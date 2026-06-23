from google.adk import Agent

def create_deploy_agent(name: str, description: str, instruction: str) -> Agent:
    """Helper factory to uniformly instantiate our DeployMind sub-agents."""
    return Agent(
        model="gemini-2.5-flash",
        name=name,
        description=description,
        instruction=instruction
    )