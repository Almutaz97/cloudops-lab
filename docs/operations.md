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

## Application Logging

ServiceOps uses Python's standard logging module.

- Logger: `serviceops`
- Format: timestamp, severity, logger name, message
- Output: stderr
- Log level: SERVICEOPS_LOG_LEVEL (default: INFO)

Application startup and shutdown events are logged automatically.

## Error Handling

Unexpected application errors:
- Return HTTP 500 with a generic message.
- Record exception details and traceback in application logs.
- Do not expose internal exception details to API clients.

## Automated Testing

Install development dependencies:

    python -m pip install -r requirements-dev.txt

Run all tests:

    python -m pytest -q

Tests cover API responses, configuration, application lifecycle,
and unexpected error handling.
