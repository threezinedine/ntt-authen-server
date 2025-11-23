from fastapi import Request, HTTPException
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

        try:
            response = await call_next(request)

            logger.info(
                f"Response status: {response.status_code} for {request.method} {request.url}"
            )
        except Exception as e:
            logger.error(
                f"Error processing request: {request.method} {request.url} - {str(e)}"
            )
            raise HTTPException(status_code=500, detail="Internal Server Error")

        return response
