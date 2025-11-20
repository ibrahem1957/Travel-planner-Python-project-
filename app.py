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

# عرض الأنواع مع أرقام
st.write("Select a trip type by number:")
for i, t in enumerate(all_trip_types, start=1):
    st.write(f"{i}. {t}")

# إدخال الميزانية
budget = st.number_input("Enter your budget (SAR):", min_value=0)

# اختيار رقم الرحلة
trip_number = st.number_input(
    f"Enter trip type number (1-{len(all_trip_types)}):",
    min_value=1,
    max_value=len(all_trip_types)
)

selected_trip = [all_trip_types[trip_number - 1]]

# زر التوصيات
if st.button("Get Recommendations"):
    getting_destination(budget, selected_trip)
