from .error_types.http_not_found_error import HttpNotFoundError 
from src.main.http_types.http_response import HttpResponse

def handle_error(errors: Exception) -> HttpResponse:
    if isinstance(errors, (HttpNotFoundError)):
        return HttpResponse(
            status_code= errors.status_code,
            body={
                "errors":[{
                    "title": errors.name,
                    "detail": errors.message,
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "error": [{
                "title": "Internal Server Error",
                "detail": str(errors)
            }]
        }
    )