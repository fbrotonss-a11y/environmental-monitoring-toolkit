# Spatial Hazard & Environmental Buffer Analysis Module
# Author: Freddy Brotons
# Open-source toolkit for agroecological risk zoning, buffer impact estimation,
# and spatial monitoring in sub-tropical vulnerable landscapes.

from typing import Dict, List


def calculate_buffer_impact_area(feature_length_m: float, buffer_distance_m: float) -> Dict[str, float]:
    """
    Calculates total influence area (buffer) along flow corridors or riverlines in m2 and hectares.
    """
    if feature_length_m <= 0 or buffer_distance_m <= 0:
        return {"error": "Dimensions must be strictly positive."}
    
    # Area calculation considering both lateral margins
    total_area_m2 = feature_length_m * (buffer_distance_m * 2.0)
    total_hectares = total_area_m2 / 10000.0
    
    return {
        "corridor_length_m": feature_length_m,
        "buffer_radius_m": buffer_distance_m,
        "impact_area_m2": round(total_area_m2, 2),
        "impact_area_ha": round(total_hectares, 4)
    }


def classify_hazard_zone(distance_to_corridor_m: float) -> Dict[str, str]:
    """
    Classifies parcel exposure and recommended land management practices based on proximity to hazard flow.
    """
    if distance_to_corridor_m <= 50.0:
        return {
            "risk_level": "CRITICAL",
            "action": "Restricted zone: Riparian restoration and native reforestation only (no settlements or intensive crops)."
        }
    elif 50.0 < distance_to_corridor_m <= 150.0:
        return {
            "risk_level": "MODERATE",
            "action": "Buffer zone: Agroforestry, soil stabilization, and runoff mitigation barriers."
        }
    else:
        return {
            "risk_level": "LOW",
            "action": "Safe agricultural zone: Standard agroecological and regenerative practices permitted."
        }


def batch_parcel_risk_assessment(parcels: List[Dict]) -> List[Dict]:
    """
    Assesses a list of agricultural parcels and assigns vulnerability status.
    """
    evaluated = []
    for p in parcels:
        assessment = classify_hazard_zone(p.get("distance_m", 0.0))
        evaluated.append({
            "parcel_id": p.get("id"),
            "distance_m": p.get("distance_m"),
            "risk_level": assessment["risk_level"],
            "recommended_action": assessment["action"]
        })
    return evaluated


if __name__ == "__main__":
    print("=== Spatial Hazard Analysis & Buffer Engine Initialized ===")
    
    # Example corridor simulation (e.g., natural drainage / hazard path)
    corridor_eval = calculate_buffer_impact_area(feature_length_m=5400.0, buffer_distance_m=100.0)
    print(f"Calculated Impact Zone: {corridor_eval['impact_area_ha']} hectares ({corridor_eval['impact_area_m2']} m2)")

    # Sample parcels assessment
    sample_parcels = [
        {"id": "Parcel-A_LaJoya", "distance_m": 35.0},
        {"id": "Parcel-B_Cancy", "distance_m": 120.0},
        {"id": "Parcel-C_Placitas", "distance_m": 350.0}
    ]
    
    results = batch_parcel_risk_assessment(sample_parcels)
    for r in results:
        print(f"[{r['parcel_id']}] Level: {r['risk_level']} -> {r['recommended_action']}")
