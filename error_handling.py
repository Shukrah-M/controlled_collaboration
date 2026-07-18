def handle_error(error):
    return {
        "status": "error",
        "error_type": type(error).__name__,
        "message": str(error)
    }
