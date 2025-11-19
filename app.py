import streamlit as st
from recommendation_logic import getting_destination
import data
import random

st.title("🌍 Travel Planner")

# إدخال المستخدم
budget = st.number_input("Enter your budget (SAR):", min_value=0)
trip_types_input = st.text_input(
    "Enter trip types (comma separated):", 
    "Culture, Beach, Adventure"
)
trip_types = [t.strip() for t in trip_types_input.split(",")]

# زر للحصول على التوصيات
if st.button("Get Recommendations"):
    # تعريف دالة طباعة التوصيات بشكل جميل
    def print_recommendations(title, recs):
        st.subheader(title)
        if recs:
            rec = random.choice(recs)
            for name, info in rec.items():
                st.markdown(f"**Destination:** {name}")
                if "country" in info:
                    st.markdown(f"**Country:** {info['country']}")
                else:
                    st.markdown(f"**Region:** {info['region']}")
                st.markdown(f"**Avg Budget/Day:** {info['average_budget_per_day']} SAR")
                st.markdown("**Activities:**")
                for act in info['activities']:
                    st.markdown(f"- {act}")
                st.markdown("---")

    # استدعاء الدالة من recommendation_logic
    # مع تعديل لتقسيم التوصيات إلى محلية وعالمية
    global_recommendations = []
    local_recommendations = []

    trip_types_lower = [t.lower() for t in trip_types]

    for des_name, des_info in data.travel_data.items():
        avg_price = des_info["average_budget_per_day"]
        if 0 <= budget - avg_price <= 100 and any(t.lower() in des_info["trip_type"] for t in trip_types):
            global_recommendations.append({des_name: des_info})

    for des_name, des_info in data.saudi_travel_data.items():
        avg_price = des_info["average_budget_per_day"]
        if 0 <= budget - avg_price <= 100 and any(t.lower() in des_info["trip_type"] for t in trip_types):
            local_recommendations.append({des_name: des_info})

    missing_types = []
    for t in trip_types:
        global_filtered = [rec for rec in global_recommendations if t in list(rec.values())[0]["trip_type"]]
        local_filtered = [rec for rec in local_recommendations if t in list(rec.values())[0]["trip_type"]]

        if global_filtered or local_filtered:
            st.subheader(f"Recommendations for {t} trip:")

        if global_filtered and local_filtered:
            print_recommendations("Global Recommendations", global_filtered)
            print_recommendations("Local Recommendations", local_filtered)
        elif global_filtered:
            print_recommendations("Global Recommendations", global_filtered)
        elif local_filtered:
            print_recommendations("Local Recommendations", local_filtered)
        else:
            missing_types.append(t)

    if missing_types:
        st.warning(f"Sorry! No recommendation matches your preferences and budget for: {', '.join(missing_types)}\nTry adjusting your budget or choosing different trip types.")
