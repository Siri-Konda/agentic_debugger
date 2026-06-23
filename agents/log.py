from agents.base import create_deploy_agent

log_analysis_agent = create_deploy_agent(
    name="LogAnalysisAgent",
    description="Reads and extracts raw errors and deployment log details into a concise summary.",
    instruction="""
    You are an expert site reliability engineer. Read the deployment/runtime logs provided by the user.
    Extract the core errors, stack traces, and warnings.
    Provide a concise summary highlighting the fundamental breaking point.
    """
)