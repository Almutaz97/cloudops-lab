#!/usr/bin/env bash

SERVICE="serviceops"
PORT="8000"
URL="http://127.0.0.1:${PORT}/health"

echo "=== ServiceOps Diagnostics ==="

# 1. Check systemd service
if systemctl is-active --quiet "$SERVICE"; then
    echo "[OK] systemd service is running"
else
    echo "[FAIL] systemd service is not running"
    exit 1
fi

# 2. Check listening port with retries
PORT_READY=0

for attempt in {1..10}; do
    if ss -H -ltn "( sport = :${PORT} )" | grep -q "127.0.0.1:${PORT}"; then
        PORT_READY=1
        break
    fi
    sleep 1
done

if [ "$PORT_READY" -eq 1 ]; then
    echo "[OK] Port ${PORT} is listening"
else
    echo "[FAIL] Port ${PORT} is not listening after retries"
    exit 1
fi


# 3. Check HTTP response
if HTTP_CODE=$(curl -sS --max-time 3 -o /dev/null \
    -w '%{http_code}' "$URL"); then

    if [ "$HTTP_CODE" = "200" ]; then
        echo "[OK] API returned HTTP 200"
    else
        echo "[FAIL] API returned HTTP ${HTTP_CODE}"
        exit 1
    fi
else
    echo "[FAIL] API connection failed"
    exit 1
fi

echo "=== All checks passed ==="
