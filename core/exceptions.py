class IndustrialAIEngineerError(Exception):
    """Base exception for Industrial AI Engineer."""
    pass


class AnalysisError(IndustrialAIEngineerError):
    """Raised when product analysis cannot be completed."""
    pass


class AgentExecutionError(IndustrialAIEngineerError):
    """Raised when an AI agent fails to execute a task."""
    pass