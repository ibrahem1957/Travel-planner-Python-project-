import streamlit as st
from recommendation_logic import getting_destination
import data
import random

st.title("🌍 Travel Planner")

# -----------------------------
# استخراج أنواع الرحلات تلقائيًا من ملفات البيانات
# -----------------------------
all_trip_types = set()

# الوجهات العالمية
for destination in data.travel_data.values():
    for t in destination["trip_type"]:
        all_trip_types.add(t.capitalize())

# الوجهات السعودية
for destination in data.saudi_travel_data.values():
    for t in destination["trip_type"]:
        all_trip_types.add(t.capitalize())

# نحولها لقائمة مرتبة
all_trip_types = sorted(list(all_trip_types))

# -----------------------------
# عرض الأنواع مع الأرقام
# -----------------------------
st.write("Select a trip type by number:")
for i, t in enumerate(all_trip_types, start=1):
    st.write(f"{i}. {t}")

# -----------------------------
# إدخال الميزانية
# -----------------------------
budget = st.number_input("Enter your budget (SAR):", min_value=0)

# -----------------------------
# اختيار نوع الرحلة
# -----------------------------
trip_number = st.number_input(
    f"Enter trip type number (1-{len(all_trip_types)}):",
    min_value=1,
    max_value=len(all_trip_types)
)

selected_trip = [all_trip_types[trip_number - 1]]  # List لأن الدالة تستقبل قائمة

# -----------------------------
# زر التوصيات
# -----------------------------
if st.button("Get Recommendations"):
    getting_destination(budget, selected_trip)
