#!/bin/bash
# Deploy to endpoints
ansible-playbook ansible/playbooks/deploy_software.yml -l production
