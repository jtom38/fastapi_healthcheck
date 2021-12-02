# fastapi_healthcheck

Easy to use health check for your FastAPI.  This is the root module that will let you add 

## Adding Health Checks

This module alone will not give you all the HealthChecks that you would need, but this gives you the factory that other modules can use.

```python
from fastapi import FastAPI
from fastapi_healthcheck import HealthCheckFactory, HealthCheckModel

app = FastAPI()

# Add Health Checks
_healthChecks = HealthCheckFactory()
_healthChecks.add(HealthCheckSQLAlchemy(alias='postgres db', connectionUri=cs.value, table=SmtpContactsSqlModel, tags=('postgres', 'db', 'sql01')))
_healthChecks.add(HealthCheckUri(alias='reddit', connectionUri="https://www.reddit.com/r/aww.json", tags=('external', 'reddit', 'aww')))
@app.get('/health')
def getHealth() -> HealthCheckModel:
    res = _healthChecks.check()
    if res['status'] == HealthCheckStatusEnum.UNHEALTHY.value:
        return JSONResponse(content=res, status_code=500)
    return JSONResponse(content=res, status_code=200)

```

This is an example of what you would add to your project

## Returned Data

When you request your health check, it will go and check all the entries that have been submited and run a basic query against them.  If they come back as expected, then a status

```json

{
    "status":"Healthy",
    "totalTimeTaken":"0:00:00.671642",
    "entities":[
        {
            "alias":"postgres db",
            "status":"Healthy",
            "timeTaken":"0:00:00.009619",
            "tags":["postgres","db","sql01"]
        },
        {
            "alias":"reddit",
            "status":"Unhealthy",
            "timeTaken":"0:00:00.661716",
            "tags":["external","reddit","aww"]
        }
    ]
}
```

## Available Modules

* [fastapi_healthcheck_sqlalchemy]()
* [fastapi_healthcheck_uri]()
    * This module will reach out with a get command and validate that data comes back.  You can use this to test external vendors or services that your application requires.

## Writing a custom module

You can easily expand on this core module to add other health checks for other services.  Generate a new service that pulls in [HealthCheckInterface]() and [HealthCheckBase]().  With those, you can build the respective class around the interface.

Once you have your service ready to go, add it to the HealthCheckFactory, and let the testing start.
