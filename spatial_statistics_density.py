# Spatial Statistics & Heatmap Density Analyzer for Precision Agriculture
# Author: Freddy Brotons
# Open-source toolkit for zonal statistics, point density estimation (heatmaps),
# and agricultural feature classification (points, lines, polygons).

import math
from typing import Dict, List, Tuple


def calculate_zonal_statistics(values: List[float]) -> Dict[str, float]:
    """
    Computes summary spatial statistics (mean, min, max, variance, std_dev)
    for sampled agricultural metrics (e.g., NDVI, soil humidity, pH).
    """
    if not values:
        return {"error": "Value list cannot be empty."}
    
    n = len(values)
    mean_val = sum(values) / n
    variance = sum((x - mean_val) ** 2 for x in values) / (n - 1) if n > 1 else 0.0
    std_dev = math.sqrt(variance)
    
    return {
        "count": n,
        "min": round(min(values), 3),
        "max": round(max(values), 3),
        "mean": round(mean_val, 3),
        "std_dev": round(std_dev, 3)
    }


def estimate_point_density(sample_points: List[Tuple[float, float]], center: Tuple[float, float], radius_m: float) -> Dict[str, float]:
    """
    Simulates a kernel/radial density estimate around a central agricultural parcel
    to determine incident clustering (pest outbreaks, tree survival points).
    """
    if radius_m <= 0:
        return {"error": "Search radius must be positive."}
    
    points_within = 0
    for pt in sample_points:
        dist = math.hypot(pt[0] - center[0], pt[1] - center[1])
        if dist <= radius_m:
            points_within += 1
            
    # Area of search window in hectares (radius in meters)
    search_area_ha = (math.pi * (radius_m ** 2)) / 10000.0
    density_per_ha = points_within / search_area_ha if search_area_ha > 0 else 0.0
    
    return {
        "points_found": points_within,
        "search_radius_m": radius_m,
        "search_area_ha": round(search_area_ha, 3),
        "density_per_ha": round(density_per_ha, 2)
    }


def summarize_vector_layers(num_points: int, line_length_m: float, polygon_area_m2: float) -> Dict[str, float]:
    """
    Consolidates basic vector geometries (points, lines, polygons)
    used in GIS parcel boundary mapping and irrigation layout.
    """
    return {
        "total_monitoring_points": num_points,
        "total_infrastructure_length_km": round(line_length_m / 1000.0, 3),
        "total_polygon_area_ha": round(polygon_area_m2 / 10000.0, 4)
    }


if __name__ == "__main__":
    print("=== Spatial Statistics & Density Engine Initialized ===")
    
    # 1. Zonal statistics test (e.g. soil moisture readings across parcels)
    readings = [18.4, 21.2, 19.8, 25.1, 22.0, 17.9, 23.4]
    stats = calculate_zonal_statistics(readings)
    print(f"Soil Moisture Summary: Mean = {stats['mean']}%, StdDev = {stats['std_dev']}")

    # 2. Kernel/Heatmap density estimation
    field_center = (0.0, 0.0)
    incidents = [(10, 15), (20, -10), (150, 200), (-30, 40), (5, 5)]
    density = estimate_point_density(sample_points=incidents, center=field_center, radius_m=100.0)
    print(f"Density within 100m: {density['density_per_ha']} points/ha ({density['points_found']} points)")

    # 3. Vector layer consolidation
    layers = summarize_vector_layers(num_points=45, line_length_m=3400.0, polygon_area_m2=85000.0)
    print(f"Vector summary: {layers['total_polygon_area_ha']} ha mapped, {layers['total_infrastructure_length_km']} km traced.")
