# agents/validator.py
from agents.base import create_deploy_agent

validation_agent = create_deploy_agent(
    name="ValidationAgent",
    description="Reviews proposed fixes for hallucinations, safety concerns, and contextual accuracy.",
    instruction="""
    You are a defensive programming reviewer. Examine the original error log summary and cross-reference it against the proposed fixes.
    Evaluate whether the fix is completely relevant or a hallucination/security hazard.
    
    Respond strictly in JSON format matching this schema:
    {
      "status": "APPROVED" or "REJECTED",
      "critique": "Explanation for why it passes review or why it failed validation."
    }
    """
)