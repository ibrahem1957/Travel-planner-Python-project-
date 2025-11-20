import streamlit as st
from recommendation_logic import getting_destination
import data

st.title("🌍 Travel Planner")

# استخراج كل أنواع الرحلات
all_trip_types = set()
for dest in list(data.travel_data.values()) + list(data.saudi_travel_data.values()):
    for t in dest["trip_type"]:
        all_trip_types.add(t.capitalize())
all_trip_types = sorted(list(all_trip_types))

# إدخال الميزانية
budget = st.number_input("Enter your budget (SAR):", min_value=0)

# اختيار أكثر من نوع رحلة
selected_numbers = st.multiselect(
    "Select one or more trip types:",
    options=list(range(1, len(all_trip_types)+1)),
    format_func=lambda x: f"{x}. {all_trip_types[x-1]}"
)

selected_trip = [all_trip_types[i-1] for i in selected_numbers]

# زر التوصيات
if st.button("Get Recommendations"):
    if selected_trip:
        getting_destination(budget, selected_trip, tolerance=100)

    else:
        st.warning("⚠️ Please select at least one trip type.")
