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

## systemd Service Management

ServiceOps runs as a systemd-managed Linux service.

Service definition: `deploy/systemd/serviceops.service`

### Installation

    sudo install -m 644 deploy/systemd/serviceops.service /etc/systemd/system/serviceops.service
    sudo systemctl daemon-reload
    sudo systemctl enable --now serviceops

The service file currently uses Ubuntu-specific absolute paths.

### Operations

Check service status:

    systemctl status serviceops

Restart the service:

    sudo systemctl restart serviceops

Stop the service:

    sudo systemctl stop serviceops

View recent logs:

    sudo journalctl -u serviceops -n 50 --no-pager

Follow logs:

    sudo journalctl -u serviceops -f

### Failure Recovery Verification

A controlled SIGKILL test confirmed:

- systemd detected the process failure.
- Restart=on-failure triggered automatic recovery.
- Uvicorn restarted with a new PID.
- The /health endpoint returned HTTP 200 after recovery.

### Current Limitations

- Service paths are specific to the local Ubuntu VM.
- Boot-time startup is enabled but has not been tested after reboot.
- No external dependency readiness checks yet.
- No container-based deployment yet.

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

## ServiceOps Diagnostic Script

Script: `scripts/serviceops-check.sh`

### Usage

    ./scripts/serviceops-check.sh

### Checks

1. Verify systemd service is active.
2. Verify TCP port 8000 is listening.
3. Verify /health returns HTTP 200.

### Reliability

- Port check retries up to 10 times.
- Exit code 0 indicates success.
- Exit code 1 indicates a failed check.
- The script diagnoses failures but does not restart services.

### Verified Scenarios

- Healthy service: all checks passed.
- Stopped service: failure detected.
- Service restart: startup timing issue identified.
- Retry logic: successful verification after restart.

