# EndpointSync Architecture

## Overview
EndpointSync is a Unified Endpoint Management (UEM) system leveraging:
- **Ansible**: Agentless configuration management for endpoints.
- **Docker**: Containerized applications for consistent deployments.
- **GitLab CI**: Automated build, test, and deploy pipelines.
- **Streamlit**: Web interface for monitoring and control.

## Components
1. **Ansible Layer**:
   - Manages endpoint configurations and software deployments.
   - Uses inventory files to define target endpoints.
   - Playbooks and roles handle tasks like Docker setup and patching.

2. **Docker Layer**:
   - Containers for security agents and management dashboards.
   - Docker Compose for multi-container setups.

3. **Streamlit UI**:
   - Provides a user-friendly interface for triggering playbooks and viewing inventory.
   - Integrates with Ansible and Docker APIs.

4. **CI/CD Layer**:
   - GitLab CI pipelines automate building and deploying containers.
   - Includes testing for playbooks and application code.

## Workflow
1. Define endpoints in `ansible/inventory/`.
2. Build Docker images via GitLab CI.
3. Deploy software using Ansible playbooks.
4. Monitor via Streamlit UI.
