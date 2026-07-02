from digital_twins.models.material import Material
from digital_twins.models.technology import Technology
from digital_twins.models.product import Product
from agents.economics_agent.cost_calculator import CostCalculator


material = Material(
    name="Aluminium 6061",
    density=2700,
    price_per_kg=12.50
)

technology = Technology(
    name="CNC Milling",
    machine_hour_rate=80,
    setup_time_minutes=20,
    accuracy_mm=0.05
)

product = Product(
    name="Robot Gripper Bracket",
    description="Детайл за закрепване на роботизиран захват.",
    material=material,
    technology=technology,
    volume_m3=0.00045,
    production_time_minutes=35,
    labor_cost=8,
    energy_cost=3,
    defect_rate_percent=4,
    desired_profit_margin_percent=25
)

calculator = CostCalculator()
result = calculator.analyze_product(product)

print(result)