
import streamlit as st

# Define stages with department responsibility and colors
stages = [
    {"stage": "RFQ / Customer Inquiry Received", "department": "Customer Success", "color": "#FFD700"},
    {"stage": "Feasibility Assessment", "department": "Technical Services / Quality / Operations", "color": "#87CEEB"},
    {"stage": "Quote Preparation", "department": "Customer Success / Technical Services / Operations / Quality", "color": "#32CD32"},
    {"stage": "Quote Sent", "department": "Customer Success", "color": "#FFD700"},
    {"stage": "Customer Decision", "department": "Customer Success", "color": "#FFD700"},
    {"stage": "Project Kickoff & Setup", "department": "Customer Success", "color": "#FFD700"},
    {"stage": "Project Plan & Packaging Plan", "department": "Customer Success / Technical Services / Quality / Operations", "color": "#32CD32"},
    {"stage": "GMP Document Creation", "department": "Technical Services / Quality / Operations", "color": "#87CEEB"},
    {"stage": "Equipment OQ & Line Trial", "department": "Technical Services / Operations / Quality", "color": "#87CEEB"},
    {"stage": "PQ Batch (GMP Run)", "department": "Operations / Technical Services / Quality", "color": "#FFA07A"},
    {"stage": "Commercial Release & Routine Production", "department": "Customer Success / Operations / Quality", "color": "#32CD32"},
    {"stage": "Ongoing Account Management", "department": "Customer Success", "color": "#FFD700"}
]

# Initialize session state
if "current_stage" not in st.session_state:
    st.session_state.current_stage = 0

# Dashboard title
st.title("📊 Customer Project Dashboard")

# Buttons to control progress
col1, col2 = st.columns([1,1])
with col1:
    if st.button("Advance Stage"):
        if st.session_state.current_stage < len(stages) - 1:
            st.session_state.current_stage += 1
with col2:
    if st.button("Reset Progress"):
        st.session_state.current_stage = 0

# Display progress bar
progress = (st.session_state.current_stage + 1) / len(stages)
st.progress(progress)

# Show all stages in a visual column layout
st.subheader("Project Workflow by Department:")

# Create columns for each department
departments = ["Customer Success", "Technical Services", "Operations", "Quality"]
cols = st.columns(len(departments))

for i, dept in enumerate(departments):
    with cols[i]:
        st.markdown(f"### {dept}")
        for idx, s in enumerate(stages):
            if dept in s["department"]:
                # Highlight current stage
                if idx == st.session_state.current_stage:
                    st.markdown(f"<div style='background-color:{s['color']};padding:5px;border-radius:5px'><b>✅ {s['stage']}</b></div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div style='background-color:{s['color']};padding:5px;border-radius:5px'>{s['stage']}</div>", unsafe_allow_html=True)