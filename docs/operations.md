# ServiceOps — Linux Operations

## Runtime
- OS: Ubuntu 22.04
- Application: FastAPI / Uvicorn
- Bind address: 127.0.0.1:8000
- Runtime user: ubuntu
- Python virtual environment: .venv

## Process Inspection
- `pgrep -af uvicorn` — Identify application processes.
- `ps -o pid,ppid,user,stat,etime,cmd -p <PID>` — Inspect process details.
- `ss -ltnp` — Inspect listening TCP ports.

## Process Management
- `kill -TERM <PID>` — Request graceful shutdown.
- Avoid SIGKILL unless graceful termination fails.

## Troubleshooting
- Port conflict: identify the process already listening.
- HTTP verification: `curl -i http://127.0.0.1:8000/health`
- Confirm that the application runs without root privileges.

## Current Limitations
- Uvicorn is started manually.
- Automatic restart is not configured.
- systemd integration is planned for Week 2.
