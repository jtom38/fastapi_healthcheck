# fastapi_healthcheck

Easy to use health check for your FastAPI.  This is the root module that will let you add implement and expand your usage of health checks, with FastAPI.

This module does not contain any service checkers, but you can easily add them.  The other modules are not in this root module due to different dependencies required for each one.  This is made so you only bring in the packages that you need to not add extra packages.

## Install

`pip install fastapi-healthcheck` or `poetry add fastapi-healthcheck`

## Adding Health Checks

Here is what you need to get started.

```python
from fastapi import FastAPI
from fastapi_healthcheck import HealthCheckFactory, healthCheckRoute
from fastapi_healthcheck_sqlalchemy import HealthCheckSQLAlchemy

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
* [fastapi_healthcheck_mongodb](https://github.com/anesmemisevic/fastapi_healthcheck_mongodb)

If you have made a public service module and want to see it on this list, please open a new issue so we can add it to the list.

## Writing a custom module

You can easily expand on this core module to add other health checks for other services.  Generate a new service that pulls in [HealthCheckInterface](https://github.com/jtom38/fastapi_healthcheck/blob/master/fastapi_healthcheck/domain.py#L6) and [HealthCheckBase](https://github.com/jtom38/fastapi_healthcheck/blob/master/fastapi_healthcheck/service.py#L75).  With those, you can build the respective class around the interface.

Once you have your service ready to go, add it to the HealthCheckFactory, and let the testing start.

If you would like to see an example of a custom service see [fastapi_healthcheck_sqlalchemy](https://github.com/jtom38/fastapi_healthcheck_sqlalchemy/blob/master/fastapi_healthcheck_sqlalchemy/service.py).  This will give you a better example of what you need to do to create your own module to interface with healthcheck.
