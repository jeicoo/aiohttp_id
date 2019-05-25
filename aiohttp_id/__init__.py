import uuid
from contextvars import ContextVar

from aiohttp.web import middleware

__all__ = [setup, REQUEST_ID]

REQUEST_ID = ContextVar('REQUEST_ID', default="---")

def setup(app, request_key='id', id_generator=uuid.uuid4):
    @middleware
    async def create_request_id(request, handler):
        request_id = str(id_generator())
        request[request_key] = request_id
        return await handler(request)

    app.middlewares.append(create_request_id)
