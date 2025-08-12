#!/bin/bash
# Run tests
pytest tests/
ansible-lint ansible/playbooks/*.yml
