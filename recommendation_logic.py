import streamlit as st
import random
import data

def getting_destination(budget, trip_types):
    results = []

    # البحث في travel_data
    for destination, info in data.travel_data.items():
        if info["price"] <= budget:
            if any(t.lower() in [tt.lower() for tt in info["trip_type"]] for t in trip_types):
                results.append((destination, info["country"], info["price"], info["trip_type"]))

    # البحث في saudi_travel_data
    for destination, info in data.saudi_travel_data.items():
        if info["price"] <= budget:
            if any(t.lower() in [tt.lower() for tt in info["trip_type"]] for t in trip_types):
                results.append((destination, info["country"], info["price"], info["trip_type"]))

    # لو ما فيه نتائج
    if not results:
        st.warning("❌ No destinations found matching your budget and trip type.")
        return

    # اختيار عشوائي من النتائج
    dest = random.choice(results)

    st.success("🎉 Recommended Destination:")
    st.write(f"**Destination:** {dest[0]}")
    st.write(f"**Country:** {dest[1]}")
    st.write(f"**Price:** {dest[2]} SAR")
    st.write(f"**Trip Types:** {', '.join(dest[3])}")
