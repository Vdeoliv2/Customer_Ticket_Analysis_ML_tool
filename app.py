from src.data_processing import load_data, validate_data
import streamlit as st
import pandas as pd
from pathlib import Path
from src.ai_analyzer import analyze_ticket
from src.classifier import train_classifier, classify_ticket
import os

LLM_ENABLED = (
    os.getenv("LLM_ENABLED", "false").lower()
    == "true"
)

# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Customer Support Analytics",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# Load data
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = (
    BASE_DIR
    / "data"
    / "processed"
    / "customer_support_tickets_clean.csv"
)

df = load_data(DATA_PATH)


# --------------------------------------------------
# Prepare resolution-time data
# --------------------------------------------------

df["Time to Resolution"] = pd.to_datetime(
    df["Time to Resolution"],
    errors="coerce"
)

df["First Response Time"] = pd.to_datetime(
    df["First Response Time"],
    errors="coerce"
)

df["Resolution Duration"] = (
    df["Time to Resolution"]
    - df["First Response Time"]
)


# --------------------------------------------------
# Application heading
# --------------------------------------------------

st.title(
    "AI-Powered Customer Support Analytics"
)

st.write(
    "Analyze historical customer-support data "
    "and evaluate incoming support tickets."
)


# --------------------------------------------------
# Navigation
# --------------------------------------------------

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Support Dashboard",
        "AI Ticket Analyzer"
    ]
)


# ==================================================
# OVERVIEW
# ==================================================

if page == "Overview":

    st.header("Project Overview")

    st.subheader("Dataset Overview")

    st.write(
        f"Total tickets: {len(df):,}"
    )

    st.dataframe(
        df.head(10),
        use_container_width=True
    )

    validation_results = validate_data(df)

    if validation_results["is_valid"]:
        st.success(
            "Dataset validation passed."
        )
    else:
        st.warning(
            "The dataset contains validation issues."
        )


# ==================================================
# SUPPORT DASHBOARD
# ==================================================

elif page == "Support Dashboard":

    st.header("Support Dashboard")

    st.write(
        "Explore historical customer-support ticket "
        "volume, satisfaction, resolution performance, "
        "and unresolved tickets."
    )


    # ----------------------------------------------
    # Filters
    # ----------------------------------------------

    selected_types = st.multiselect(
        "Ticket Type",
        options=sorted(
            df["Ticket Type"]
            .dropna()
            .unique()
        )
    )

    selected_priorities = st.multiselect(
        "Ticket Priority",
        options=sorted(
            df["Ticket Priority"]
            .dropna()
            .unique()
        )
    )


    # ----------------------------------------------
    # Create filtered DataFrame
    # ----------------------------------------------

    filtered_df = df.copy()

    if selected_types:
        filtered_df = filtered_df[
            filtered_df["Ticket Type"].isin(
                selected_types
            )
        ]

    if selected_priorities:
        filtered_df = filtered_df[
            filtered_df["Ticket Priority"].isin(
                selected_priorities
            )
        ]


    # ----------------------------------------------
    # Handle empty filter result
    # ----------------------------------------------

    if filtered_df.empty:

        st.warning(
            "No tickets match the selected filters."
        )

    else:

        # ------------------------------------------
        # Unresolved tickets
        # ------------------------------------------

        unresolved_mask = (
            filtered_df["Resolution"].isna()
            |
            filtered_df["Resolution"]
            .fillna("")
            .str.strip()
            .eq("")
            |
            filtered_df["Resolution"]
            .fillna("")
            .str.strip()
            .str.lower()
            .eq("not resolved")
        )

        unresolved_df = filtered_df[
            unresolved_mask
        ]


        # ------------------------------------------
        # High and critical unresolved tickets
        # ------------------------------------------

        normalized_priority = (
            filtered_df["Ticket Priority"]
            .fillna("")
            .str.strip()
            .str.lower()
        )

        high_unresolved_df = filtered_df[
            unresolved_mask
            & normalized_priority.eq("high")
        ]

        critical_unresolved_df = filtered_df[
            unresolved_mask
            & normalized_priority.eq("critical")
        ]

        # ------------------------------------------
        # KPI calculations
        # ------------------------------------------

        total_tickets = len(filtered_df)

        unresolved_tickets = len(
            unresolved_df
        )

        high_unresolved_count = len(
            high_unresolved_df
        )

        critical_unresolved_count = len(
            critical_unresolved_df
        )

        average_satisfaction = (
            filtered_df[
                "Customer Satisfaction Rating"
            ]
            .mean()
        )

        valid_resolution_duration = (
            filtered_df[
                filtered_df["Resolution Duration"]
                >= pd.Timedelta(0)
            ]
        )

        average_resolution_time = (
            valid_resolution_duration[
                "Resolution Duration"
            ]
            .mean()
        )


        # ------------------------------------------
        # KPI cards
        # ------------------------------------------

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Total Tickets",
                f"{total_tickets:,}"
            )

        with col2:
            st.metric(
                "Unresolved Tickets",
                f"{unresolved_tickets:,}"
            )

        with col3:
            st.metric(
                "High Unresolved",
                f"{high_unresolved_count:,}"
            )

        with col4:
            st.metric(
                "Critical Unresolved",
                f"{critical_unresolved_count:,}"
            )


        col5, col6 = st.columns(2)

        with col5:
            st.metric(
                "Average Satisfaction",
                f"{average_satisfaction:.2f}"
            )

        with col6:
            if pd.notna(average_resolution_time):
                resolution_hours = (
                    average_resolution_time
                    / pd.Timedelta(hours=1)
                )

                st.metric(
                    "Average Resolution Time",
                    f"{resolution_hours:.2f} hours"
                )
            else:
                st.metric(
                    "Average Resolution Time",
                    "N/A"
                )


        # ------------------------------------------
        # Ticket volume
        # ------------------------------------------

        st.subheader(
            "Ticket Volume by Type"
        )

        ticket_volume = (
            filtered_df["Ticket Type"]
            .value_counts()
        )

        st.bar_chart(
            ticket_volume
        )


        # ------------------------------------------
        # Satisfaction analysis
        # ------------------------------------------

        st.subheader(
            "Average Satisfaction by Type"
        )

        satisfaction_by_type = (
            filtered_df
            .groupby("Ticket Type")[
                "Customer Satisfaction Rating"
            ]
            .mean()
            .sort_values(ascending=False)
        )

        st.bar_chart(
            satisfaction_by_type
        )


        # ------------------------------------------
        # Resolution-time analysis
        # ------------------------------------------

        st.subheader(
            "Average Resolution Time by Type"
        )

        resolution_by_type = (
            valid_resolution_duration
            .groupby("Ticket Type")[
                "Resolution Duration"
            ]
            .mean()
        )

        resolution_hours_by_type = (
            resolution_by_type
            / pd.Timedelta(hours=1)
        )

        st.bar_chart(
            resolution_hours_by_type
        )


        # ------------------------------------------
        # Unresolved ticket details
        # ------------------------------------------

        st.subheader(
            "Unresolved Ticket Details"
        )

        st.dataframe(
            unresolved_df,
            use_container_width=True
        )


        # ------------------------------------------
        # Ticket details
        # ------------------------------------------

        st.subheader(
            "Ticket Details"
        )

        st.dataframe(
            filtered_df,
            use_container_width=True
        )


# ==================================================
# AI TICKET ANALYZER
# ==================================================

elif page == "AI Ticket Analyzer":

    st.header("AI Ticket Analyzer")

    st.write(
        "Enter a customer-support ticket to analyze "
        "its category, sentiment, urgency, and summary."
    )

    # ----------------------------------------------
    # Ticket input
    # ----------------------------------------------

    ticket_description = st.text_area(
        "Ticket Description",
        placeholder=(
            "Example: I was charged twice for my "
            "purchase and need a refund."
        ),
        height=150
    )

    analyze_button = st.button(
        "Analyze Ticket"
    )


    # ----------------------------------------------
    # Run analysis when button is clicked
    # ----------------------------------------------

    if analyze_button:

        # Validate input
        cleaned_description = ticket_description.strip()

        if cleaned_description == "":

            st.warning(
                "Please enter a ticket description."
            )

        elif not any(
            character.isalpha()
            for character in cleaned_description
        ):

            st.warning(
                "Please enter a meaningful ticket description."
            )

        else:

            try:

                # ----------------------------------
                # Traditional ML prediction
                # ----------------------------------

                vectorizer, model = train_classifier(
                    DATA_PATH
                )

                ml_prediction = classify_ticket(
                    ticket_description,
                    vectorizer,
                    model
                )


                # ----------------------------------
                # LLM analysis
                # ----------------------------------

                with st.spinner(
                    "Analyzing ticket..."
                ):

                    analysis = analyze_ticket(
                        ticket_description
                    )


                # ----------------------------------
                # AI analysis results
                # ----------------------------------

                st.subheader(
                    "AI Analysis"
                )

                st.write(
                    "**Summary:**",
                    analysis["Summary"]
                )

                st.write(
                    "**Category:**",
                    analysis["Category"]
                )

                st.write(
                    "**Sentiment:**",
                    analysis["Sentiment"]
                )

                st.write(
                    "**Urgency:**",
                    analysis["Urgency"]
                )


                # ----------------------------------
                # Classification comparison
                # ----------------------------------

                st.subheader(
                    "Classification Comparison"
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "Traditional ML",
                        ml_prediction
                    )

                with col2:

                    st.metric(
                        "Llama 3.1",
                        analysis["Category"]
                    )


            except Exception as error:

                st.error(
                    f"Ticket analysis failed: {error}"
                )
