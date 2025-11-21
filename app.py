
import streamlit as st
from recommendation_logic import getting_destination
import data

# Full Modern UI Theme
st.markdown("""
<style>

    /* ===== خلفية الصفحة كاملة ===== */
    .stApp {
    background-color: #f5f7fa !important;
}


    /* عنوان كبير جميل */
    h1 {
        text-align: center;
        color: #1b3b5f !important;
        font-size: 38px !important;
        font-weight: 800 !important;
        margin-bottom: 15px !important;
    }

    /* النصوص */
    .css-10trblm, .css-1q8dd3e {
        color: #123 !important;
        font-size: 18px !important;
    }

    /* ===== صندوق الاختيارات ===== */
    .stSelectbox, .stMultiSelect, .stNumberInput {
        background: #ffffff !important;
        padding: 10px;
        border-radius: 12px !important;
        box-shadow: 0px 3px 10px rgba(0,0,0,0.06);
    }

    /* ===== زر التوصيات ===== */
    .stButton button {
        background: linear-gradient(90deg, #0077ff, #00c6ff);
        color: white;
        padding: 12px 20px;
        font-size: 20px;
        border-radius: 12px;
        border: none;
        transition: 0.3s ease-in-out;
        font-weight: 600;
        width: 100%;
    }
    .stButton button:hover {
        background: linear-gradient(90deg, #005bd1, #00a3cc);
        transform: scale(1.02);
    }

    /* ===== صندوق التوصيات ===== */
    .trip-box {
        background: white;
        padding: 18px;
        border-radius: 14px;
        margin-bottom: 15px;
        box-shadow: 0px 6px 16px rgba(0,0,0,0.1);
        border-left: 6px solid #007bff;
    }

    .trip-box h3 {
        color: #004a85;
        margin-bottom: 8px;
    }

    /* خط فاصل */
    hr {
        border: none;
        height: 1px;
        background: #cccccc;
        margin: 20px 0;
    }

</style>
""", unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center; color:#333;'>🌍 Travel Planner</h1>", unsafe_allow_html=True)

# استخراج أنواع الرحلات من البيانات
all_trip_types = set()

for dest in data.travel_data.values():
    for t in dest["trip_type"]:
        all_trip_types.add(t.capitalize())

for dest in data.saudi_travel_data.values():
    for t in dest["trip_type"]:
        all_trip_types.add(t.capitalize())

all_trip_types = sorted(list(all_trip_types))

with st.sidebar:
    st.header("🧭 Trip Filters")
    selected_trip_types = st.multiselect("Trip Types", all_trip_types)
    budget = st.number_input("Daily Budget (SAR per day):", min_value=0)

    st.write("---")
    run = st.button("Get Recommendations")


if run:
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
                st.subheader("🌍 Global Recommendations: ")
                for r in global_rec:
                    for name, info in r.items():
                        st.markdown(f"""
                            <div class="trip-box">
                                <h3>{name}</h3>
                                <p><b>Country:</b> {info.get('country', '-')}</p>
                                <p><b>Budget/day:</b> {info['average_budget_per_day']} SAR</p>
                                <p><b>Activities:</b> {", ".join(info['activities'])}</p>
                            </div>
                        """, unsafe_allow_html=True)


            if local_rec:
                st.subheader("SA Saudi Recommendations: ")
                for r in local_rec:
                    for name, info in r.items():
                        st.markdown(f"""
                            <div class="trip-box">
                                <h3>{name}</h3>
                                <p><b>Region:</b> {info.get('region', '-')}</p>
                                <p><b>Budget/day:</b> {info['average_budget_per_day']} SAR</p>
                                <p><b>Activities:</b> {", ".join(info['activities'])}</p>
                            </div>
                        """, unsafe_allow_html=True)


        # الأنواع اللي ما لها نتائج
        if missing:
            st.warning("⚠️ No matches for: " + ", ".join(missing))
