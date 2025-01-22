def success_response(message: str):
    return {"status": "success", "message": message}

def error_response(message: str):
    return {"status": "error", "message": message}
