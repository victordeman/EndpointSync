# EndpointSync Setup Guide

## Installation
1. Install prerequisites:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip docker.io ansible git
   pip install -r streamlit/requirements.txt
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/victordeman/EndpointSync
   cd EndpointSync
   ```

3. Configure Ansible:
   - Update `ansible/inventory/production.yml` with your endpoint details.
   - Secure SSH keys and update `ansible/group_vars/all.yml` as needed.

4. Build Docker images:
   ```bash
   docker build -t localhost:5000/security-agent:latest docker/security-agent/
   docker build -t localhost:5000/management-dashboard:latest docker/management-dashboard/
   ```

5. Start Streamlit:
   ```bash
   streamlit run streamlit/app.py
   ```

## Troubleshooting
- **Ansible SSH errors**: Ensure SSH keys are configured and endpoints are reachable.
- **Docker issues**: Verify Docker service is running (`sudo systemctl status docker`).
- **Streamlit errors**: Check `requirements.txt` dependencies are installed.
