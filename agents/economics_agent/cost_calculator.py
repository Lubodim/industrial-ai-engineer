from digital_twins.models.product import Product
from digital_twins.models.analysis_result import AnalysisResult
from engineering.formulas import (
    calculate_material_cost,
    calculate_machine_cost,
    calculate_defect_cost,
    calculate_total_cost,
    calculate_selling_price,
    calculate_profit,
    calculate_profit_margin,
)


class CostCalculator:
    def analyze_product(self, product: Product) -> AnalysisResult:
        if product.mass_kg is None:
            product.calculate_mass()

        if product.mass_kg is None:
            raise ValueError("Product mass cannot be calculated. Please provide volume_m3.")

        material_cost = calculate_material_cost(
            mass_kg=product.mass_kg,
            price_per_kg=product.material.price_per_kg
        )

        machine_cost = calculate_machine_cost(
            machine_hour_rate=product.technology.machine_hour_rate,
            production_time_minutes=product.production_time_minutes
        )

        base_cost = material_cost + machine_cost + product.labor_cost + product.energy_cost

        defect_cost = calculate_defect_cost(
            base_cost=base_cost,
            defect_rate_percent=product.defect_rate_percent
        )

        total_cost = calculate_total_cost(
            material_cost=material_cost,
            machine_cost=machine_cost,
            labor_cost=product.labor_cost,
            energy_cost=product.energy_cost,
            defect_cost=defect_cost
        )

        selling_price = calculate_selling_price(
            total_cost=total_cost,
            desired_profit_margin_percent=product.desired_profit_margin_percent
        )

        expected_profit = calculate_profit(
            selling_price=selling_price,
            total_cost=total_cost
        )

        profit_margin_percent = calculate_profit_margin(
            profit=expected_profit,
            selling_price=selling_price
        )

        return AnalysisResult(
            material_cost=round(material_cost, 2),
            machine_cost=round(machine_cost, 2),
            labor_cost=round(product.labor_cost, 2),
            energy_cost=round(product.energy_cost, 2),
            total_cost=round(total_cost, 2),
            selling_price=round(selling_price, 2),
            expected_profit=round(expected_profit, 2),
            profit_margin_percent=round(profit_margin_percent, 2),
            quality_risk=self._estimate_quality_risk(product),
            production_risk=self._estimate_production_risk(product),
            recommendations=self._generate_basic_recommendations(product)
        )

    def _estimate_quality_risk(self, product: Product) -> str:
        if product.defect_rate_percent >= 10:
            return "Висок риск от брак"
        if product.defect_rate_percent >= 5:
            return "Среден риск от брак"
        return "Нисък риск от брак"

    def _estimate_production_risk(self, product: Product) -> str:
        if product.production_time_minutes > 120:
            return "Високо производствено време"
        if product.production_time_minutes > 45:
            return "Средно производствено време"
        return "Ниско производствено време"

    def _generate_basic_recommendations(self, product: Product) -> list[str]:
        recommendations = []

        if product.defect_rate_percent > 5:
            recommendations.append("Да се анализират причините за повишения процент брак.")

        if product.production_time_minutes > 60:
            recommendations.append("Да се разгледа възможност за оптимизация на технологичния процес.")

        if product.material.price_per_kg > 20:
            recommendations.append("Да се проучат алтернативни материали с по-ниска цена.")

        if not recommendations:
            recommendations.append("Показателите са в приемливи граници.")

        return recommendations