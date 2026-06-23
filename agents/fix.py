from agents.base import create_deploy_agent

fix_suggestion_agent = create_deploy_agent(
    name="FixSuggestionAgent",
    description="Suggests structural steps and configuration edits to fix classified deployment issues.",
    instruction="""
    Based on the parsed log analysis and the classified issue category, generate up to two highly applicable, concrete solutions.
    Provide clear explanations and the reasoning behind each step.
    
    Respond strictly in JSON format matching this schema:
    {
      "proposed_fixes": [
         {
           "fix_id": 1,
           "title": "Short title of fix",
           "steps": "Step by step execution details",
           "reasoning": "Why this fix resolves the structural error"
         }
      ]
    }
    """
)