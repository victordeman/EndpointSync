# EndpointSync

A Unified Endpoint Management (UEM) system for automated software distribution and endpoint management using Docker, GitLab CI, and Ansible.

## Overview
EndpointSync is designed to manage software deployment, configuration, and patching across hybrid endpoints (Windows, macOS, Linux). It provides a lightweight, open-source alternative to tools like Baramundi and SCCM.

## Setup
1. Clone the repository: `git clone https://github.com/victordeman/EndpointSync`
2. Install dependencies: `pip install -r streamlit/requirements.txt`
3. Configure Ansible inventory in `ansible/inventory/`.
4. Run the Streamlit UI: `streamlit run streamlit/app.py`

## Directory Structure
- `ansible/`: Ansible playbooks, roles, and inventory for endpoint management.
- `docker/`: Docker configurations for containerized applications.
- `streamlit/`: Streamlit-based management interface.
- `ci/`: GitLab CI pipelines for automation.
- `docs/`: Documentation.
- `tests/`: Unit and integration tests.

## License
MIT License
