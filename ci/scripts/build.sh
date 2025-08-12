#!/bin/bash
# Build Docker images
docker build -t localhost:5000/security-agent:latest docker/security-agent/
docker build -t localhost:5000/management-dashboard:latest docker/management-dashboard/
docker push localhost:5000/security-agent:latest
docker push localhost:5000/management-dashboard:latest
