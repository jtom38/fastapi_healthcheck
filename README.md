# fastapi_healthcheck

Easy to use health check for your FastAPI.  This is the root module that will let you add implement and expand your usage of health checks, with FastAPI.

This module does not contain any service checkers, but you can easily add them.  The other modules are not in this root module due to different dependencies required for each one.  This is made so you only bring in the packages that you need to not add extra packages.

## Adding Health Checks

Here is what you need to get started.

```python
from fastapi import FastAPI
from fastapi_healthcheck import HealthCheckFactory, healthCheckRoute

app = FastAPI()

# Add Health Checks
_healthChecks = HealthCheckFactory()

# SQLAlchemy comes from fastapi-healthcheck-sqlalchemy
_healthChecks.add(HealthCheckSQLAlchemy(alias='postgres db', connectionUri=cs.value, table=SmtpContactsSqlModel, tags=('postgres', 'db', 'sql01')))

# This will check external URI and validate the response that is returned.
# fastapi-healthcheck-uri
_healthChecks.add(HealthCheckUri(alias='reddit', connectionUri="https://www.reddit.com/r/aww.json", tags=('external', 'reddit', 'aww')))
app.add_api_route('/health', endpoint=healthCheckRoute(factory=_healthChecks))

```

## Returned Data

When you request your health check, it will go and check all the entries that have been submitted and run a basic query against them.  If they come back as expected, then a status code is 200.  But if it runs into an error, it will return a 500 error.

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

* [fastapi_healthcheck_sqlalchemy](https://github.com/jtom38/fastapi_healthcheck_sqlalchemy)
* [fastapi_healthcheck_uri](https://github.com/jtom38/fastapi_healthcheck_uri)

## Writing a custom module

You can easily expand on this core module to add other health checks for other services.  Generate a new service that pulls in [HealthCheckInterface]() and [HealthCheckBase]().  With those, you can build the respective class around the interface.

Once you have your service ready to go, add it to the HealthCheckFactory, and let the testing start.
