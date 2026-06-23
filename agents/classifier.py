from agents.base import create_deploy_agent

issue_classification_agent = create_deploy_agent(
    name="IssueClassificationAgent",
    description="Categorizes log summaries into predefined issue buckets.",
    instruction="""
    You analyze text log summaries and categorize them into exactly one of these buckets:
    - Dependency Error
    - Build Error
    - Runtime Error
    - Configuration Error

    Respond strictly in JSON format matching this schema:
    {
      "category": "One of the 4 buckets above",
      "confidence": "High/Medium/Low",
      "root_cause": "Brief description"
    }
    """
)