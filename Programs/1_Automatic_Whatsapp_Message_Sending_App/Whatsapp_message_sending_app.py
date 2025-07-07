# import os
# from pathlib import Path

# script_path = Path(__file__).resolve().parent / "Home.py"
# os.system(f"streamlit run {script_path}")


import os
from pathlib import Path

# Ensure the script path includes the .py extension
script_path = Path(__file__).resolve().parent / "Home.py"

# Run Streamlit in headless mode
os.system(f'streamlit run "{script_path}"')
