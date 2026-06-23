import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.log import log_analysis_agent

def test_single_agent():
    print("Testing LogAnalysisAgent locally...")
    sample_log = "[ERROR] Connection timeout at database cluster."
    res = log_analysis_agent.run(sample_log)
    print(res)

if __name__ == "__main__":
    test_single_agent()