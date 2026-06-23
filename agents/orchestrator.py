from google.adk import Workflow
from agents.log import log_analysis_agent
from agents.classifier import issue_classification_agent
from agents.fix import fix_suggestion_agent
from agents.validator import validation_agent

root_agent = Workflow(
    name="DeployMindOrchestrator",
    edges=[
        ("START", log_analysis_agent),
        (log_analysis_agent, issue_classification_agent),
        (issue_classification_agent, fix_suggestion_agent),
        (fix_suggestion_agent, validation_agent)
    ]
)