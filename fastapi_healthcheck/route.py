from typing import Callable
from starlette.responses import Response, JSONResponse
from .service import HealthCheckFactory
from .enum import HealthCheckStatusEnum


def healthCheckRoute(factory: HealthCheckFactory) -> Callable:
    """
    This function is passed to the add_api_route with the built factory.

    When called, the endpoint method within, will be called and it will run the job bound to the factory.
    The results will be parsed and sent back to the requestor via JSON.
    """
    
    _factory = factory

    def endpoint() -> Response:
        res = _factory.check()    
        if res['status'] == HealthCheckStatusEnum.UNHEALTHY.value:
            return JSONResponse(content=res, status_code=500)
        return JSONResponse(content=res, status_code=200)

    return endpoint

