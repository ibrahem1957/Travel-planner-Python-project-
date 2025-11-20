import streamlit as st
from recommendation_logic import getting_destination
import data

st.title("🌍 Travel Planner")

# استخراج كل أنواع الرحلات من travel_data و saudi_travel_data
all_trip_types = set()

for destination in data.travel_data.values():
    for t in destination["trip_type"]:
        all_trip_types.add(t.capitalize())

for destination in data.saudi_travel_data.values():
    for t in destination["trip_type"]:
        all_trip_types.add(t.capitalize())

# تحويلها لقائمة مرتبة
all_trip_types = sorted(list(all_trip_types))

# اختيار متعدد لأنواع الرحلات
selected_trips = st.multiselect(
    "Select one or more trip types:",
    all_trip_types
)

# إدخال الميزانية
budget = st.number_input("Enter your budget (SAR):", min_value=0)

# زر التوصيات
if st.button("Get Recommendations"):
    if not selected_trips:
        st.warning("⚠️ Please select at least one trip type.")
    else:
        getting_destination(budget, selected_trips)
