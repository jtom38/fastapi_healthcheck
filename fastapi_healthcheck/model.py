from datetime import datetime
from typing import List, Optional, Union
from .enum import HealthCheckStatusEnum
from datetime import datetime
from pydantic import BaseModel


class HealthCheckEntityModel(BaseModel):
    alias: str
    #service: str
    status: Union[HealthCheckStatusEnum, str] = HealthCheckStatusEnum.HEALTHY 
    timeTaken: Union[Optional[datetime], str]
    tags: List[str] = list()


class HealthCheckModel(BaseModel):
    status: Union[HealthCheckStatusEnum, str] = HealthCheckStatusEnum.HEALTHY
    totalTimeTaken:  Union[Optional[datetime], str]
    entities: List[HealthCheckEntityModel] = list()



