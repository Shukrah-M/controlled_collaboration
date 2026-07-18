from datetime import datetime, timezone


def create_log(message):
    timestamp = datetime.now(timezone.utc).isoformat()

    return {
        "timestamp": timestamp,
        "message": message
    }
