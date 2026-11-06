# CloudOps Lab

**A hands-on Cloud Infrastructure and DevOps Engineering project**

## Overview

CloudOps Lab is an evolving engineering project focused on designing, deploying, automating, securing, and monitoring cloud-native applications.

The goal is to develop practical skills in Linux, Networking, Docker, AWS, Terraform, Kubernetes, CI/CD, GitOps, and Observability through a single progressively developed system.

## Current Implementation — Phase 1

The initial version contains a simple Python REST API built with FastAPI and served by Uvicorn.

**Implemented:**
- Python virtual environment and dependency management
- FastAPI application with a health endpoint
- Uvicorn HTTP application server
- Local API testing with curl
- SSH local port forwarding for remote access
- Git version control and GitHub repository

## Quick Start

**Requirements:** Linux, Python 3.10+, Git.

1. Clone the repository and enter its directory.
2. Create the environment: `python3 -m venv .venv`
3. Activate it: `source .venv/bin/activate`
4. Install dependencies: `python -m pip install -r requirements.txt`
5. Start the API: `uvicorn main:app --host 127.0.0.1 --port 8000`
6. Test it: `curl -i http://127.0.0.1:8000/health`

**Expected response:**

`{"status":"ok"}`

The health endpoint currently verifies that the application can respond to HTTP requests. It does not validate external dependencies.

## Planned Development

- Containerization with Docker and Docker Compose
- PostgreSQL integration and Nginx reverse proxy
- AWS infrastructure provisioning using Terraform
- CI/CD automation with GitHub Actions
- Kubernetes deployment with Helm
- GitOps deployment using Argo CD
- Monitoring and logging
- Security hardening, incident troubleshooting, and operational documentation

These capabilities will be implemented and documented incrementally.

## Engineering Approach

Each phase prioritizes reproducible deployment, practical troubleshooting, version control, security awareness, and clear technical documentation.

**Status:** Work in progress — Phase 1.
