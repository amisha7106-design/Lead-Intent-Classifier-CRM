import streamlit as st
import pandas as pd

from classifier import predict_intent
from crm import save_lead


st.set_page_config(
    page_title="Lead Intent Classifier CRM",
    page_icon="📩",
    layout="wide"
)

st.title("📩 Lead Intent Classifier CRM")
st.write("Enter a lead message and AI will automatically identify its intent.")

# -------------------------
# Sidebar
# -------------------------

st.sidebar.title("📊 CRM Navigation")

page = st.sidebar.radio(
    "Select Page",
    ["Classify Lead", "Admin Dashboard"]
)


# =====================================================
# CLASSIFY LEAD
# =====================================================

if page == "Classify Lead":

    st.header("📝 Lead Information")

    name = st.text_input("Lead Name")
    email = st.text_input("Email Address")

    message = st.text_area(
        "Lead Message",
        placeholder="Example: I want to know the pricing of your product..."
    )

    if st.button("🔍 Classify Lead", type="primary"):

        if not name or not email or not message:
            st.warning("Please fill in all the fields.")

        else:

            # Predict intent
            intent = predict_intent(message)

            # Save lead
            save_lead(
                name=name,
                email=email,
                message=message,
                intent=intent
            )

            st.success("✅ Lead classified and saved successfully!")

            st.subheader("🎯 Prediction")

            st.info(f"Lead Intent: **{intent}**")


# =====================================================
# ADMIN DASHBOARD
# =====================================================

elif page == "Admin Dashboard":

    st.header("📊 Admin Dashboard")

    file_path = "data/leads.csv"

    try:

        df = pd.read_csv(file_path)

        # Total leads
        total_leads = len(df)

        # Intent counts
        intent_counts = df["intent"].value_counts()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("👥 Total Leads", total_leads)

        with col2:
            st.metric(
                "💰 Pricing Leads",
                intent_counts.get("Pricing", 0)
            )

        with col3:
            st.metric(
                "🛠 Support Leads",
                intent_counts.get("Support", 0)
            )

        st.divider()

        st.subheader("📌 Intent Distribution")

        st.bar_chart(intent_counts)

        st.subheader("📋 All Leads")

        st.dataframe(
            df,
            use_container_width=True
        )

    except FileNotFoundError:

        st.warning("No leads found yet. Please classify a lead first.")