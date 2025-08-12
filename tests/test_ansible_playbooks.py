import pytest
import yaml
import os

def test_inventory_file():
    assert os.path.exists("ansible/inventory/production.yml")
    with open("ansible/inventory/production.yml", "r") as f:
        inventory = yaml.safe_load(f)
        assert "all" in inventory
        assert "endpoint1" in inventory["all"]["hosts"]

def test_playbook_exists():
    assert os.path.exists("ansible/playbooks/deploy_software.yml")
