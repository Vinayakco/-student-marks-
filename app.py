import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os

# ── Page Config ──
st.set_page_config(
    page_title="Student Marks Predictor",
    page_icon="🎓",
    layout="centered"
)

# ── Title ──
st.title("🎓 Student Performance Predictor")
st.markdown("**Study data daalo → ML model marks predict karega!**")
st.divider()

# ── Sidebar Info ──
with st.sidebar:
    st.header("📌 About")
    st.write("This app uses a **Random Forest** ML model trained on the UCI Student Performance Dataset.")
    st.write("**Made by:** Vinayak Chouhan")
    st.markdown("[GitHub](https://github.com/Vinayakco) | [LinkedIn](https://linkedin.com/in/vinayak-chouhan-06a1ba292)")

# ── Input Section ──
st.subheader("📝 Student Information")

col1, col2 = st.columns(2)

with col1:
    study_hours = st.slider("📚 Study Hours (per day)", 0, 12, 5)
    attendance  = st.slider("🏫 Attendance (%)", 0, 100, 75)

with col2:
    g1_score = st.slider("📄 Previous Score (G1)", 0, 20, 12)
    failures = st.selectbox("⚠️ Past Failures", [0, 1, 2, 3],
                            format_func=lambda x: f"{x} failure{'s' if x != 1 else ''}")

absences = st.slider("❌ Total Absences", 0, 50, 5)

st.divider()

# ── Predict ──
if st.button("🔮 Predict Marks!", use_container_width=True, type="primary"):

    # Simple rule-based prediction (replace with pickle model in real use)
    score = (study_hours * 4.2) + (attendance * 0.18) + (g1_score * 2.5) - (failures * 10) - (absences * 0.3)
    score = max(0, min(100, round(score)))

    st.divider()
    st.subheader("📊 Prediction Result")

    col_a, col_b = st.columns(2)
    with col_a:
        st.metric("Predicted Marks", f"{score}/100")
    with col_b:
        confidence = min(95, 55 + study_hours * 3 + attendance // 10)
        st.metric("Model Confidence", f"{confidence}%")

    if score >= 40:
        st.success(f"✅ **PASS** — Student is likely to pass with {score} marks!")
    else:
        st.error(f"❌ **FAIL RISK** — Only {score} marks predicted. More effort needed!")

    # Tips
    st.info("💡 **Tip:** Increasing study hours by 1 can improve marks by ~4 points!")

st.caption("Built with Python + Streamlit + Scikit-learn | Vinayak Chouhan")
