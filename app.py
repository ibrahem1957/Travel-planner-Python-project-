import streamlit as st
from recommendation_logic import getting_destination
import data
import random

st.title("🌍 Travel Planner")

# قراءة أنواع الرحلات من data.py
all_trip_types = list(data.travel_types.keys())  # لو عندك dict أو قائمة في data.py

# عرض الأنواع مع الأرقام
st.write("Select a trip type by number:")
for i, t in enumerate(all_trip_types, start=1):
    st.write(f"{i}. {t}")

# إدخال الميزانية
budget = st.number_input("Enter your budget (SAR):", min_value=0)

# اختيار رقم الرحلة
trip_number = st.number_input(f"Enter trip type number (1-{len(all_trip_types)}):", min_value=1, max_value=len(all_trip_types))
selected_trip = [all_trip_types[trip_number - 1]]  # نحولها لقائمة لتتناسب مع الدالة

# زر للحصول على التوصيات
if st.button("Get Recommendations"):
    getting_destination(budget, selected_trip)
