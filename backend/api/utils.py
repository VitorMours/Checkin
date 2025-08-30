def validate_json_header(request):
    if request.headers["Content-Type"] != "application/json":
        return False
    return True