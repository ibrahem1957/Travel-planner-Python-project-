import data
import random
import streamlit as st
def getting_destination(budget, selected_trip, tolerance=100):
    global_recommendations = []
    local_recommendations = []

    trip_types_lower = [t.lower() for t in trip_types]

    # البحث في الوجهات العالمية
    for des_name, des_info in data.travel_data.items():
        avg_price = des_info["average_budget_per_day"]
        if abs(budget - avg_price) <= tolerance and any(t in des_info["trip_type"] for t in trip_types_lower):
            global_recommendations.append({des_name: des_info})

    # البحث في الوجهات السعودية
    for des_name, des_info in data.saudi_travel_data.items():
        avg_price = des_info["average_budget_per_day"]
        if abs(budget - avg_price) <= tolerance and any(t in des_info["trip_type"] for t in trip_types_lower):
            local_recommendations.append({des_name: des_info})

    any_found = False

    # عرض النتائج لكل نوع رحلة
    for t in trip_types_lower:
        global_filtered = [rec for rec in global_recommendations if t in list(rec.values())[0]["trip_type"]]
        local_filtered = [rec for rec in local_recommendations if t in list(rec.values())[0]["trip_type"]]

        if global_filtered or local_filtered:
            any_found = True
            st.subheader(f"Recommendations for {t.capitalize()} trip:")

        if global_filtered:
            print_recommendations("Global Recommendations", global_filtered)
        if local_filtered:
            print_recommendations("Local Recommendations", local_filtered)

    if not any_found:
        st.warning(f"⚠️ No recommendations match your budget ({budget} SAR ±{tolerance}) and selected trip types: {', '.join(trip_types)}.")

def print_recommendations(title, recs):
    st.markdown(f"### {title}")
    rec = random.choice(recs)
    for name, info in rec.items():
        st.markdown(f"**Destination:** {name}")
        if "country" in info:
            st.markdown(f"**Country:** {info['country']}")
        else:
            st.markdown(f"**Region:** {info['region']}")
        st.markdown(f"**Avg Budget/Day:** {info['average_budget_per_day']} SAR")
        st.markdown("**Activities:**")
        for act in info["activities"]:
            st.markdown(f"- {act}")
        st.markdown("---")
