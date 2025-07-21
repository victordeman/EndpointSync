# EndpointSync

**EndpointSync** is an open-source Unified Endpoint Management (UEM) system for automated software distribution, configuration, and patch management across Windows, macOS, Linux, and IoT devices. Powered by Docker, GitLab CI, Ansible, and a Streamlit web interface, it offers a lightweight, scalable alternative to commercial tools like Baramundi and SCCM.

## Key Features
- **Automated Deployments**: Ansible and Docker ensure consistent software rollouts.
- **Configuration Management**: Agentless automation for endpoint compliance.
- **Patch Management**: Streamlined security updates and patches.
- **Web Dashboard**: Streamlit UI for monitoring and managing endpoints.
- **CI/CD Pipelines**: GitLab CI for automated build, test, and deploy workflows.

## Getting Started
1. Clone: `git clone https://github.com/victordeman/EndpointSync`
2. Install dependencies: `pip install -r streamlit/requirements.txt`
3. Run Streamlit: `streamlit run streamlit/app.py`
4. See `docs/setup.md` for detailed setup instructions.

## Documentation
Full details in `docs/`:
- [Setup Guide](docs/setup.md)
- [Architecture](docs/architecture.md)

## License
MIT License
