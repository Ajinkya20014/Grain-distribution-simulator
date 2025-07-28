import streamlit as st
import pandas as pd
from io import BytesIO

import os, sys

# ensure the folder containing app.py is on Python's import path
sys.path.append(os.path.dirname(__file__))

from simulation import run_simulation

# Page configuration
st.set_page_config(page_title="Grain Distribution Simulator", layout="wide")

st.title("Grain Distribution Simulator")
st.markdown(
    "Upload your Central Godown (CG), Local Godown (LG), and Fair Price Shop (FPS) files to run the distribution simulation."
)

# File uploaders
cg_file = st.file_uploader("Upload Central Godown file (Excel)", type=["xlsx", "xls"], key="cg")
lg_file = st.file_uploader("Upload Local Godown file (Excel)", type=["xlsx", "xls"], key="lg")
fps_file = st.file_uploader("Upload Fair Price Shop file (Excel)", type=["xlsx", "xls"], key="fps")

run_button = st.button("Run Simulation")

if run_button:
    if not (cg_file and lg_file and fps_file):
        st.error("Please upload all three files to proceed.")
    else:
        try:
            # Read uploaded files
            cg_df = pd.read_excel(cg_file)
            lg_df = pd.read_excel(lg_file)
            fps_df = pd.read_excel(fps_file)

            # Run the simulation
            output = run_simulation(cg_df, lg_df, fps_df)

            # If simulation returns multiple DataFrames, handle accordingly
            if isinstance(output, dict):
                # Prepare a BytesIO buffer
                buffer = BytesIO()
                with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
                    for sheet_name, df in output.items():
                        df.to_excel(writer, sheet_name=sheet_name, index=False)
                    writer.save()
                buffer.seek(0)
                st.success("Simulation completed successfully!")
                st.download_button(
                    label="Download Results as Excel", 
                    data=buffer, 
                    file_name="simulation_results.xlsx", 
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            else:
                # Single DataFrame
                buffer = BytesIO()
                df = output
                df.to_excel(buffer, index=False)
                buffer.seek(0)
                st.success("Simulation completed successfully!")
                st.download_button(
                    label="Download Results as Excel", 
                    data=buffer, 
                    file_name="simulation_results.xlsx", 
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

        except Exception as e:
            st.error(f"An error occurred during simulation: {e}")
