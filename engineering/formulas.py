def calculate_material_cost(mass_kg: float, price_per_kg: float) -> float:
    return mass_kg * price_per_kg


def calculate_machine_cost(machine_hour_rate: float, production_time_minutes: float) -> float:
    return machine_hour_rate * (production_time_minutes / 60)


def calculate_defect_cost(base_cost: float, defect_rate_percent: float) -> float:
    return base_cost * (defect_rate_percent / 100)


def calculate_total_cost(
    material_cost: float,
    machine_cost: float,
    labor_cost: float,
    energy_cost: float,
    defect_cost: float
) -> float:
    return material_cost + machine_cost + labor_cost + energy_cost + defect_cost


def calculate_selling_price(total_cost: float, desired_profit_margin_percent: float) -> float:
    return total_cost * (1 + desired_profit_margin_percent / 100)


def calculate_profit(selling_price: float, total_cost: float) -> float:
    return selling_price - total_cost


def calculate_profit_margin(profit: float, selling_price: float) -> float:
    if selling_price == 0:
        return 0
    return (profit / selling_price) * 100