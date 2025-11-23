from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from app.core import logger
from typing import Callable, Awaitable


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self,
        request: Request,
        call_next: Callable[
            [Request],
            Awaitable[Response],
        ],
    ) -> Response:
        logger.info(f"Incoming request: {request.method} {request.url}")

        response = await call_next(request)

        logger.info(
            f"Response status: {response.status_code} for {request.method} {request.url}"
        )

        return response
