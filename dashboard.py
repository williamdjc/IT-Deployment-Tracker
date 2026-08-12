import streamlit as st
import sqlite3 

conn = sqlite3.connect("projects.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM projects")
projects = cursor.fetchall()

st.title("IT Deployment Tracker")
st.caption("Track deployment progress, device completion, project health, and open issues.")
total_projects = len(projects)
total_devices = sum(project[4] for project in projects)
completed_devices = sum(project[5] for project in projects)
open_issues = sum(project[6] for project in projects)
overall_progress = (completed_devices / total_devices) * 100 if total_devices > 0 else 0

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total Projects", total_projects)

with col2:
    st.metric("Total Devices", total_devices)

with col3:
    st.metric("Completed Devices", completed_devices)

with col4:
    st.metric("Open Issues", open_issues)
with col5:
    st.metric("Overall Progress", f"{overall_progress:.1f}%")
st.subheader("Project Overview")
for project in projects:
    st.markdown(f"### {project[1]}")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(f"**Client:** {project[2]}")
        st.write(f"**Location:** {project[3]}")

    with col2:
        st.write(f"**Status:** {project[8]}")
        st.write(f"**Health:** {project[9]}")

    with col3:
        st.write(f"**Progress:** {project[7]:.1f}%")

    st.progress(min(project[7] / 100, 1.0))
    st.divider()