import os
from dotenv import load_dotenv
from agents.orchestrator import root_agent
from memory import DeployMindMemory
import time
import re

load_dotenv()

def human_approval_gate(agent_output: str) -> bool:
    """Bonus Challenge: Human-in-the-Loop Approval Agent Gate"""
    print("HUMAN-IN-THE-LOOP APPROVAL REQUIRED")
    print("─" * 45)
    print(f"Proposed Fix Summary:\n{agent_output}")
    print("─" * 45)
    
    choice = input("Authorize agent deployment script execution? (yes/no): ").strip().lower()
    return choice in ['yes', 'y']

def run_with_retry(agent, prompt: str, max_retries: int = 3):
    """Run the agent and retry on HTTP 503 responses.

    If the exception message contains a Retry-After value it will be used as the
    wait time (in seconds). Otherwise an exponential backoff is used (capped).
    """
    attempt = 0
    while True:
        try:
            return agent.run(input=prompt)
        except Exception as e:
            msg = str(e)
            # Detect common 503 indicators
            if '503' in msg or 'Service Unavailable' in msg or 'service_unavailable' in msg.lower():
                # Try to extract a Retry-After header value from the error text
                m = re.search(r'Retry-After[:=]\s*(\d+)', msg, re.I) or re.search(r'retry[-_ ]?after[:=]\s*(\d+)', msg, re.I)
                wait = int(m.group(1)) if m else None
                # fallback to exponential backoff (1,2,4,8...) capped at 60s
                if wait is None:
                    wait = min(60, 2 ** attempt)

                attempt += 1
                if attempt > max_retries:
                    print(f"Max retries reached ({max_retries}). Raising the last exception.")
                    raise

                print(f"Received 503 from LLM. Waiting {wait} seconds before retrying (attempt {attempt}/{max_retries})...")
                time.sleep(wait)
                continue
            # If it's not a 503-like error, re-raise immediately
            raise

def run_pipeline():
    memory_layer = DeployMindMemory()
    log_dir = "logs"
    
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        print(f" Created empty '{log_dir}' directory. Place your mock logs inside it.")
        return

    print("🚀 Initializing DeployMind Multi-Agent Production Pipeline...\n")
    
    log_files = [f for f in os.listdir(log_dir) if f.endswith(".log")]
    if not log_files:
        print("No log files found in the 'logs/' folder to evaluate.")
        return

    for file_name in log_files:
        file_path = os.path.join(log_dir, file_name)
        print("=" * 60)
        print(f" EVALUATING LOG PROFILE: {file_name}")
        print("=" * 60)
        
        with open(file_path, "r") as f:
            log_content = f.read()

        # Historical Cache Memory Lookup
        mem_hit = memory_layer.check_memory(log_content)
        if mem_hit:
            print(f"{mem_hit} (Optimized Short-Circuit)\n")
            continue

        # Feed log context to the multi-agent graph
        try:
            prompt = f"Triage and propose validated solutions for this incident report log:\n{log_content}"
            # Use the retry helper which respects Retry-After or falls back to exponential backoff
            result = run_with_retry(root_agent, prompt)
            
            output_text = getattr(result, 'text', str(result))
            print("\n🤖 [Pipeline Workflow Output]:")
            print(output_text)
            
            # Step 3: Human Verification Checkpoint
            if "APPROVED" in output_text or '"status": "APPROVED"' in output_text:
                if human_approval_gate(output_text):
                    print("Execution Authorized. Patch applied successfully to the environment!")
                    memory_layer.save_memory(file_name, "Verified patch applied cleanly via human approval workflow.")
                else:
                    print("Execution Denied. Deployment patch safely rejected by developer action.")
            else:
                print("Workflow Stopped: The Validation Agent rejected this fix proposal.")
                
        except Exception as e:
            print(f" Execution tracking error on {file_name}: {e}")
        print("\n")

if __name__ == "__main__":
    run_pipeline()