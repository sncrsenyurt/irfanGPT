import streamlit as st
import pandas as pd

# Load the CSV file
solutions = pd.read_csv('troubleshooting_solutions.csv')

# Streamlit title and input
st.title('Troubleshooting Guide')
st.write("Please check your issue on CoreDash and follow the steps below.")

# Get user input for the issue description
issue_description = st.text_input('What is your issue? (e.g., steeringTrackingLost, camera_internal_state_error, etc.)')

if issue_description:
    # Find the matching solution
    solution_row = solutions[solutions['issue_description'].str.contains(issue_description, case=False, na=False)]
    if not solution_row.empty:
        st.write(f"Solution: {solution_row.iloc[0]['solution'].replace('\\n', '\n')}")
    else:
        st.write("No solution found for the specified issue.")
