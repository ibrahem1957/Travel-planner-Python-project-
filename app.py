
import streamlit as st
from recommendation_logic import getting_destination
import data

# Custom CSS
st.markdown("""
    <style>
        .main {
            background-color: #f4f6f9;
            padding: 20px;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            height: 50px;
            font-size: 18px;
            border: none;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        .trip-box {
            background: white;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 10px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)


st.title("🌍 Travel Planner")

# استخراج أنواع الرحلات من البيانات
all_trip_types = set()

for dest in data.travel_data.values():
    for t in dest["trip_type"]:
        all_trip_types.add(t.capitalize())

for dest in data.saudi_travel_data.values():
    for t in dest["trip_type"]:
        all_trip_types.add(t.capitalize())

all_trip_types = sorted(list(all_trip_types))

st.write("### Select one or more trip types:")
selected_trip_types = st.multiselect("Trip Types", all_trip_types)

budget = st.number_input("Enter your budget (SAR):", min_value=0)

if st.button("Get Recommendations"):
    if not selected_trip_types:
        st.warning("⚠️ Please select at least one trip type.")
    else:
        result = getting_destination(budget, selected_trip_types, tolerance=100)

        global_rec = result["global"]
        local_rec = result["local"]
        missing = result["missing_types"]

        # لو ما في ولا أي نتيجة
        if not global_rec and not local_rec:
            st.error("❌ No matching destinations within your budget ±100 SAR.")
        else:
            # عرض النتائج
            if global_rec:
                st.subheader("🌍 Global Recommendations")
                for r in global_rec:
                    for name, info in r.items():
                        st.write(f"**{name}** — {info['country']}")
                        st.write(f"Budget/day: {info['average_budget_per_day']} SAR")
                        st.write("Activities:")
                        st.write(", ".join(info["activities"]))
                        st.write("---")

            if local_rec:
                st.subheader("🇸🇦 Saudi Recommendations")
                for r in local_rec:
                    for name, info in r.items():
                        st.write(f"**{name}** — {info['region']}")
                        st.write(f"Budget/day: {info['average_budget_per_day']} SAR")
                        st.write("Activities:")
                        st.write(", ".join(info["activities"]))
                        st.write("---")

        # الأنواع اللي ما لها نتائج
        if missing:
            st.warning("⚠️ No matches for: " + ", ".join(missing))
