import streamlit as st
import random
import data

def getting_destination(budget, trip_types):
    import streamlit as st
    import random
    import data

    # Normalize trip types to lowercase
    trip_types = [t.lower() for t in trip_types]

    results = []

    # البحث في travel_data (عالمي)
    for destination, info in data.travel_data.items():
        avg = info.get("average_budget_per_day")
        if avg is None:
            continue
        if avg <= budget and any(t in [x.lower() for x in info.get("trip_type", [])] for t in trip_types):
            results.append((destination, info, "global"))

    # البحث في saudi_travel_data (محلي)
    for destination, info in data.saudi_travel_data.items():
        avg = info.get("average_budget_per_day")
        if avg is None:
            continue
        if avg <= budget and any(t in [x.lower() for x in info.get("trip_type", [])] for t in trip_types):
            results.append((destination, info, "local"))

    if not results:
        st.warning("❌ No destinations found matching your budget and trip type.")
        return

    # اختيار عشوائي وطباعته بشكل مرتب
    dest_name, dest_info, scope = random.choice(results)

    st.success("🎉 Recommended Destination:")
    st.markdown(f"**Destination:** {dest_name}")
    # country موجود بالـ global، region موجود بالـ local
    if scope == "global" and "country" in dest_info:
        st.markdown(f"**Country:** {dest_info['country']}")
    elif scope == "local" and "region" in dest_info:
        st.markdown(f"**Region:** {dest_info['region']}")
    st.markdown(f"**Avg Budget/Day:** {dest_info.get('average_budget_per_day', 'N/A')} SAR")
    st.markdown("**Activities:**")
    for act in dest_info.get("activities", []):
        st.markdown(f"- {act}")
    st.markdown(f"**Trip Types:** {', '.join(dest_info.get('trip_type', []))}")
