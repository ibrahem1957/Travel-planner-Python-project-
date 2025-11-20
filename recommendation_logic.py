import data
import random

def getting_destination(budget, trip_types, tolerance=100):
    global_recommendations = []
    local_recommendations = []

    # تأكد أن trip_types قائمة وليس None
    if not trip_types:
        return {
            "global": [],
            "local": [],
            "missing_types": trip_types
        }

    # تحويل الأنواع إلى lowercase
    trip_types_lower = [t.lower() for t in trip_types]

    # البحث في الوجهات العالمية
    for des_name, des_info in data.travel_data.items():
        avg_price = des_info["average_budget_per_day"]
        trip_list = des_info["trip_type"]

        if abs(budget - avg_price) <= tolerance and any(t in trip_list for t in trip_types_lower):
            global_recommendations.append({des_name: des_info})

    # البحث في الوجهات السعودية
    for des_name, des_info in data.saudi_travel_data.items():
        avg_price = des_info["average_budget_per_day"]
        trip_list = des_info["trip_type"]

        if abs(budget - avg_price) <= tolerance and any(t in trip_list for t in trip_types_lower):
            local_recommendations.append({des_name: des_info})

    # أنواع لم يتم العثور عليها
    missing_types = []
    for t in trip_types_lower:
        if not any(t in d[list(d.keys())[0]]["trip_type"] for d in global_recommendations + local_recommendations):
            missing_types.append(t)

    # إرجاع النتائج
    return {
        "global": global_recommendations,
        "local": local_recommendations,
        "missing_types": missing_types
    }
