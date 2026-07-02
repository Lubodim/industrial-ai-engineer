from agents.orchestrator.orchestrator import AgentOrchestrator
from core.exceptions import AnalysisError
from digital_twins.models.product import Product


class IndustrialAIEngine:
    """
    Central application engine.

    This class provides a single entry point for product analysis.
    GUI, CLI and future APIs should communicate with this class instead of
    calling agents directly.
    """

    def __init__(self) -> None:
        self.orchestrator = AgentOrchestrator()

    def analyze_product(self, product: Product):
        try:
            return self.orchestrator.execute(
                user_request="Calculate cost, price and profit",
                product=product
            )
        except Exception as exc:
            raise AnalysisError(f"Product analysis failed: {exc}") from exc

    def ask(self, user_request: str, product: Product):
        try:
            return self.orchestrator.execute(user_request, product)
        except Exception as exc:
            raise AnalysisError(f"Agent execution failed: {exc}") from exc