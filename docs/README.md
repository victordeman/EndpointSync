# EndpointSync

EndpointSync is an open-source Unified Endpoint Management (UEM) system designed for automated software distribution, configuration management, and patch deployment across hybrid environments (Windows, macOS, Linux, and IoT devices). Built with modern DevOps tools—Docker, GitLab CI, Ansible, and a Streamlit-based web interface—EndpointSync offers a lightweight, scalable alternative to commercial UEM solutions like Baramundi and Microsoft SCCM.

## Features
- **Automated Software Deployment**: Use Ansible playbooks and Docker containers to deploy software consistently across diverse endpoints.
- **Configuration Management**: Enforce endpoint configurations and compliance policies with Ansible’s agentless automation.
- **Patch Management**: Automate patch rollouts and security updates, mirroring SCCM’s capabilities.
- **Web Interface**: A Streamlit-based dashboard for monitoring endpoints, triggering deployments, and viewing inventory.
- **CI/CD Integration**: GitLab CI pipelines for building, testing, and deploying software updates.
- **Scalability**: Cloud-native design supports on-premises and cloud-hosted endpoints without heavy infrastructure.

## Repository Structure
```
EndpointSync/
├── ansible/                # Ansible playbooks, roles, and inventory for endpoint management
├── docker/                 # Docker configurations for containerized applications
├── streamlit/              # Streamlit web interface for management and monitoring
├── ci/                     # GitLab CI pipelines and scripts
├── docs/                   # Documentation (architecture, setup, etc.)
├── tests/                  # Unit and integration tests
└── .gitignore              # Git ignore file
```

## Prerequisites
- **System Requirements**:
  - Linux-based system (Ubuntu/Debian recommended)
  - Python 3.11+ and pip
  - Docker and Docker Compose
  - Ansible
  - Git
- **Optional**: GitLab account for CI/CD integration

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/victordeman/EndpointSync
   cd EndpointSync
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r streamlit/requirements.txt
   sudo apt update && sudo apt install docker.io ansible
   ```

3. **Configure Ansible Inventory**:
   - Edit `ansible/inventory/production.yml` and `staging.yml` to define your endpoints (e.g., host IPs, groups).
   - Example `production.yml`:
     ```yaml
     all:
       hosts:
         endpoint1:
           ansible_host: 192.168.1.10
           ansible_user: admin
         endpoint2:
           ansible_host: 192.168.1.11
           ansible_user: admin
       vars:
         ansible_connection: ssh
     ```

4. **Set Up Docker**:
   - Ensure Docker is running: `sudo systemctl start docker`
   - Build sample containers in `docker/security-agent/` and `docker/management-dashboard/`:
     ```bash
     docker build -t security-agent docker/security-agent/
     ```

5. **Run the Streamlit Interface**:
   ```bash
   streamlit run streamlit/app.py
   ```
   Access the UI at `http://localhost:8501` to manage endpoints, deploy software, or view inventory.

6. **Configure GitLab CI** (Optional):
   - Push the repository to GitLab.
   - Configure runners for `.gitlab-ci.yml` to automate build, test, and deploy stages.

## Usage
- **Streamlit Dashboard**:
  - **Dashboard**: View endpoint status (e.g., Ansible ping results).
  - **Deploy Software**: Select an Ansible playbook (e.g., `deploy_software.yml`) and target group to deploy software.
  - **View Inventory**: Display endpoint details in a table format.
- **Ansible Playbooks**:
  - Run playbooks manually: `ansible-playbook ansible/playbooks/deploy_software.yml -l all`
  - Customize playbooks in `ansible/playbooks/` for specific deployment tasks.
- **Docker Containers**:
  - Deploy containerized applications (e.g., security agents) using `docker/compose/docker-compose.yml`.
- **CI/CD Pipelines**:
  - Use `.gitlab-ci.yml` to automate building Docker images, testing playbooks, and deploying updates.

## Example Workflow
1. Add a new endpoint to `ansible/inventory/production.yml`.
2. Update `ansible/playbooks/deploy_software.yml` to install a containerized application.
3. Run the playbook via the Streamlit UI or CLI.
4. Monitor deployment status in the Streamlit dashboard or GitLab CI pipeline logs.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature`.
3. Commit changes: `git commit -m "Add your feature"`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a pull request.

Please follow the [Code of Conduct](docs/CODE_OF_CONDUCT.md) and include tests in `tests/` for new features.

## License
MIT License. See [LICENSE](LICENSE) for details.

## Contact
For issues or questions, open an issue on GitHub or contact the maintainer at [victordeman@example.com](mailto:victordeman@example.com).

---
EndpointSync v1.0 | Built with ❤️ by the EndpointSync team
