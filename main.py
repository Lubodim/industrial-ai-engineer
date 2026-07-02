from core.industrial_ai_engine import IndustrialAIEngine
from digital_twins.models.material import Material
from digital_twins.models.product import Product
from digital_twins.models.technology import Technology


def main() -> None:
    material = Material(
        name="Aluminium 6061",
        density=2700,
        price_per_kg=12.50,
    )

    technology = Technology(
        name="CNC Milling",
        machine_hour_rate=80,
        setup_time_minutes=20,
        accuracy_mm=0.05,
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
        desired_profit_margin_percent=25,
    )

    engine = IndustrialAIEngine()
    result = engine.analyze_product(product)

    print("=== Industrial AI Engineer ===")
    print(f"Product: {product.name}")
    print(f"Material cost: {result.material_cost} BGN")
    print(f"Machine cost: {result.machine_cost} BGN")
    print(f"Total cost: {result.total_cost} BGN")
    print(f"Selling price: {result.selling_price} BGN")
    print(f"Expected profit: {result.expected_profit} BGN")
    print(f"Profit margin: {result.profit_margin_percent}%")
    print(f"Quality risk: {result.quality_risk}")
    print(f"Production risk: {result.production_risk}")
    print("Recommendations:")
    for recommendation in result.recommendations:
        print(f"- {recommendation}")


if __name__ == "__main__":
    main()