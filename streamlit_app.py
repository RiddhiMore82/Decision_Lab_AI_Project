import streamlit as st

from agents.planner import planner_agent
from agents.financial import financial_agent
from agents.risk import risk_agent
from agents.devil import devil_agent
from agents.synthesizer import synthesizer_agent

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="Decision Lab",
    page_icon="🧠",
    layout="wide"
)

# --------------------------------------------------
# Session State
# --------------------------------------------------

defaults = {
    "decision": "",
    "planner": None,
    "answers": {},
    "reports": None,
    "final_report": None,
    "analysis_started": False
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.title("🧠 Decision Lab")

    st.markdown("---")

    st.subheader("AI Board Members")

    st.write("💰 Financial Analyst")
    st.write("⚠️ Risk Analyst")
    st.write("😈 Devil's Advocate")
    st.write("🏛 Chairperson")

    st.markdown("---")

    st.info(
        "An AI-powered multi-agent boardroom that helps you make better decisions."
    )

    st.markdown("---")

    if st.button("🔄 Start New Analysis"):

        for key, value in defaults.items():
            st.session_state[key] = value

        st.rerun()

# --------------------------------------------------
# Main UI
# --------------------------------------------------

st.title("🧠 Decision Lab")

st.write(
    "Consult an AI Boardroom before making important life decisions."
)

st.divider()

decision = st.text_area(
    "What decision are you trying to make?",
    value=st.session_state.decision,
    placeholder="Example: Should I buy a house?"
)

# --------------------------------------------------
# Analyze
# --------------------------------------------------

if st.button("🚀 Analyze Decision"):

    if decision.strip() == "":
        st.warning("Please enter a decision.")
        st.stop()

    st.session_state.decision = decision

    with st.spinner("Planner Agent is analyzing..."):

        planner = planner_agent(decision)

    if not isinstance(planner, dict):

        st.error(planner)
        st.stop()

    st.session_state.planner = planner
    st.session_state.analysis_started = True

    st.session_state.answers = {}
    st.session_state.reports = None
    st.session_state.final_report = None

# --------------------------------------------------
# Planner Report
# --------------------------------------------------

if st.session_state.analysis_started:

    planner = st.session_state.planner

    st.success("Planner completed!")

    st.divider()

    st.header("📋 Planner Report")

    c1, c2 = st.columns(2)

    with c1:
        st.metric("Category", planner["decision_category"])

    with c2:
        st.metric("Risk Level", planner["risk_level"])

    st.subheader("🎯 Objective")
    st.info(planner["objective"])

    st.subheader("👥 Experts")

    experts = planner.get("experts", [])

    if experts:

        cols = st.columns(len(experts))

        for i, expert in enumerate(experts):
            cols[i].success(expert.title())

    st.divider()

    # --------------------------------------------------
    # Clarification Form
    # --------------------------------------------------

    st.header("❓ Additional Information")

    questions = planner.get("missing_information", [])

    if st.session_state.reports is None:

        with st.form("clarification_form"):

            answers = {}

            for question in questions:
                answers[question] = st.text_input(question)

            submitted = st.form_submit_button(
                "🚀 Continue to AI Board Meeting"
            )

        if submitted:

            st.session_state.answers = answers

            reports = {}

            st.divider()

            st.header("👥 AI Board Meeting")

            # Financial

            if "financial" in experts:

                with st.spinner("Financial Analyst..."):

                    reports["financial"] = financial_agent(
                        st.session_state.decision,
                        planner,
                        answers
                    )

            # Risk

            if "risk" in experts:

                with st.spinner("Risk Analyst..."):

                    reports["risk"] = risk_agent(
                        st.session_state.decision,
                        planner,
                        answers
                    )

            # Devil

            if "devil" in experts:

                with st.spinner("Devil's Advocate..."):

                    reports["devil"] = devil_agent(
                        st.session_state.decision,
                        planner,
                        answers
                    )

            st.session_state.reports = reports

            with st.spinner("Chairperson is preparing the final verdict..."):

                st.session_state.final_report = synthesizer_agent(
                    st.session_state.decision,
                    planner,
                    reports
                )

            st.rerun()

# --------------------------------------------------
# Display Reports
# --------------------------------------------------

if st.session_state.reports is not None:

    reports = st.session_state.reports

    st.divider()

    st.header("👥 AI Board Meeting")

    if "financial" in reports:

        with st.expander("💰 Financial Analyst", expanded=True):
            st.markdown(reports["financial"])

    if "risk" in reports:

        with st.expander("⚠️ Risk Analyst"):
            st.markdown(reports["risk"])

    if "devil" in reports:

        with st.expander("😈 Devil's Advocate"):
            st.markdown(reports["devil"])

    st.divider()

    st.header("🏛 Board Verdict")

    with st.container(border=True):
        st.markdown(st.session_state.final_report)

    st.success("✅ Decision analysis completed!")