
import streamlit as st

# Page setup
st.set_page_config(page_title="Customer Project Dashboard", layout="wide")
st.title("📊 Customer Project Dashboard")
st.header("Project Workflow by Department")

# Departments, workflow steps, and colors
departments = {
    "Customer Success": {
        "steps": [
            "RFQ / Customer Inquiry Received",
            "Quote Preparation",
            "Quote Sent",
            "Customer Decision",
            "Project Kickoff & Setup",
            "Project Plan & Packaging Plan",
            "Commercial Release & Routine Production",
            "Ongoing Account Management"
        ],
        "color": "#FFB347"  # orange
    },
    "Technical Services": {
        "steps": [
            "Feasibility Assessment",
            "Quote Preparation",
            "Project Plan & Packaging Plan",
            "GMP Document Creation",
            "Equipment OQ & Line Trial",
            "PQ Batch (GMP Run)"
        ],
        "color": "#85C1E9"  # blue
    },
    "Operations": {
        "steps": [
            "Feasibility Assessment",
            "Quote Preparation",
            "Project Plan & Packaging Plan",
            "GMP Document Creation",
            "Equipment OQ & Line Trial",
            "PQ Batch (GMP Run)",
            "Commercial Release & Routine Production"
        ],
        "color": "#82E0AA"  # green
    },
    "Quality": {
        "steps": [
            "Feasibility Assessment",
            "Quote Preparation",
            "Project Plan & Packaging Plan",
            "GMP Document Creation",
            "Equipment OQ & Line Trial",
            "PQ Batch (GMP Run)",
            "Commercial Release & Routine Production"
        ],
        "color": "#F1948A"  # red
    }
}

# Display each department as a colored section with progress bars
for dept, data in departments.items():
    st.subheader(dept)
    steps = data["steps"]
    color = data["color"]
    
    for i, step in enumerate(steps):
        progress = (i + 1) / len(steps)
        st.markdown(f"**{step}**")
        st.progress(progress)

# Footer
st.markdown("---")
st.markdown("Generated with Streamlit 🚀")