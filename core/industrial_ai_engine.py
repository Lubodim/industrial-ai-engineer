from agents.economics_agent.cost_calculator import CostCalculator
from core.exceptions import AnalysisError
from digital_twins.models.analysis_result import AnalysisResult
from digital_twins.models.product import Product


class IndustrialAIEngine:
    """
    Central application engine.

    This class provides a single entry point for product analysis.
    GUI, CLI and future APIs should communicate with this class instead of
    calling agents directly.
    """

    def __init__(self) -> None:
        self.cost_calculator = CostCalculator()

    def analyze_product(self, product: Product) -> AnalysisResult:
        """
        Analyze a digital twin product and return an analysis result.
        """
        try:
            return self.cost_calculator.analyze_product(product)
        except Exception as exc:
            raise AnalysisError(f"Product analysis failed: {exc}") from exc