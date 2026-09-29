# Environmental Metrics and Watershed Monitoring Toolkit
# Open-source utilities for ecological tracking and environmental impact metrics.

import math


def calculate_reforestation_survival_rate(planted: int, survived: int):
    # Calculates survival and mortality rates of planted species
    if planted <= 0:
        return {"error": "Planted count must be greater than zero"}
    survival_rate = (survived / planted) * 100.0
    mortality_rate = 100.0 - survival_rate
    return {
        "total_planted": planted,
        "total_survived": survived,
        "survival_percentage": round(survival_rate, 2),
        "mortality_percentage": round(mortality_rate, 2),
    }


def estimate_riparian_buffer_area(river_length_m: float, buffer_width_m: float = 30.0):
    # Estimates riparian protection buffer area (both margins)
    if river_length_m <= 0 or buffer_width_m <= 0:
        return {"error": "Measurements must be positive numbers"}
    total_area_m2 = river_length_m * buffer_width_m * 2.0
    total_hectares = total_area_m2 / 10000.0
    return {
        "buffer_width_m": buffer_width_m,
        "total_area_m2": round(total_area_m2, 2),
        "total_area_ha": round(total_hectares, 4),
    }


def soil_organic_matter_status(som_percentage: float):
    # Categorizes soil health status based on Soil Organic Matter
    if som_percentage < 2.0:
        return "Degraded / Low organic content - Urgent remediation required"
    elif 2.0 <= som_percentage < 4.0:
        return "Moderate - Suitable for agroecological transition"
    else:
        return "Healthy / High organic content - Optimal baseline"


if __name__ == "__main__":
    print("=== Ecological Monitoring Module Initialized ===")
    reforestation = calculate_reforestation_survival_rate(500, 435)
    print(f"Reforestation metrics: {reforestation}")
    buffer = estimate_riparian_buffer_area(1200, 30)
    print(f"Riparian buffer needed: {buffer['total_area_ha']} hectares")
