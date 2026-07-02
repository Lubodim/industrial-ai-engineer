from enum import Enum


class TaskType(Enum):
    ECONOMIC_ANALYSIS = "economic_analysis"
    PRODUCTION_ANALYSIS = "production_analysis"
    AI_RECOMMENDATION = "ai_recommendation"
    UNKNOWN = "unknown"


class TaskRouter:
    def route(self, user_request: str) -> TaskType:
        request = user_request.lower()

        if any(word in request for word in ["cost", "price", "profit", "себестойност", "цена", "печалба"]):
            return TaskType.ECONOMIC_ANALYSIS

        if any(word in request for word in ["production", "time", "cycle", "производство", "време", "цикъл"]):
            return TaskType.PRODUCTION_ANALYSIS

        if any(word in request for word in ["recommend", "improve", "препоръка", "подобри", "оптимизирай"]):
            return TaskType.AI_RECOMMENDATION

        return TaskType.UNKNOWN