import streamlit as st
import pandas as pd
import subprocess
import yaml
import docker
import os

st.set_page_config(page_title="EndpointSync", layout="wide")

st.title("EndpointSync - Unified Endpoint Management")

# Sidebar for navigation
st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Select Action", ["Dashboard", "Deploy Software", "View Inventory"])

# Initializeneeded for Docker client
try:
    client = docker.from_env()
except Exception as e:
    st.error(f"Failed to connect to Docker: {e}")

# Load Ansible inventory
def load_inventory(file_path):
    try:
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        st.error(f"Error loading inventory: {e}")
        return {}

# Dashboard page
if page == "Dashboard":
    st.header("EndpointSync Dashboard")
    st.write("Overview of managed endpoints and deployment status.")
    if st.button("Refresh Status"):
        st.write("Fetching endpoint status...")
        # Placeholder for endpoint status (e.g., Ansible fact gathering)
        try:
            result = subprocess.run(["ansible", "-m", "ping", "all"], capture_output=True, text=True)
            st.write(result.stdout)
        except Exception as e:
            st.error(f"Error pinging endpoints: {e}")

# Deploy Software page
elif page == "Deploy Software":
    st.header("Deploy Software")
    playbook = st.selectbox("Select Playbook", ["deploy_software.yml", "configure_endpoint.yml", "patch_management.yml"])
    target = st.text_input("Target Group", "all")
    if st.button("Run Deployment"):
        st.write(f"Running {playbook} on {target}...")
        try:
            result = subprocess.run(["ansible-playbook", f"ansible/playbooks/{playbook}", "-l", target], capture_output=True, text=True)
            st.write(result.stdout)
            if result.stderr:
                st.error(result.stderr)
        except Exception as e:
            st.error(f"Error running playbook: {e}")

# View Inventory page
elif page == "View Inventory":
    st.header("Endpoint Inventory")
    inventory = load_inventory("ansible/inventory/production.yml")
    if inventory:
        df = pd.DataFrame.from_dict(inventory, orient='index')
        st.dataframe(df)
    else:
        st.warning("No inventory data available.")

st.sidebar.markdown("---")
st.sidebar.write("EndpointSync v1.0 | [GitHub](https://github.com/victordeman/EndpointSync)")
