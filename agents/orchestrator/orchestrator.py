from agents.economics_agent.cost_calculator import CostCalculator
from agents.orchestrator.task_router import TaskRouter, TaskType
from digital_twins.models.product import Product


class AgentOrchestrator:
    """
    Coordinates different agents in the system.
    """

    def __init__(self) -> None:
        self.router = TaskRouter()
        self.cost_calculator = CostCalculator()

    def execute(self, user_request: str, product: Product):
        task_type = self.router.route(user_request)

        if task_type == TaskType.ECONOMIC_ANALYSIS:
            return self.cost_calculator.analyze_product(product)

        if task_type == TaskType.PRODUCTION_ANALYSIS:
            return {
                "message": "Production analysis agent is not implemented yet."
            }

        if task_type == TaskType.AI_RECOMMENDATION:
            return {
                "message": "Internal AI Engineer agent is not implemented yet."
            }

        return {
            "message": "The requested task cannot be routed to an available agent."
        }