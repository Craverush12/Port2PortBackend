from datetime import datetime
from typing import Optional
from dateutil.parser import parse

from pydantic import BaseModel, EmailStr, NaiveDatetime, FutureDatetime, field_validator

class AuctionCreate(BaseModel):
    description: str
    start_time: datetime
    end_time: datetime
    initial_price: float
    good_id: int

    # @field_validator('start_time', mode="after")
    # def parse_start_date(cls, value):
    #     return parse(value)
    
    # @field_validator('end_time', mode="after")
    # def parse_end_date(cls, value):
    #     return parse(value)


class AuctionUpdate(BaseModel):
    id: int
    description: str
    start_time: datetime
    end_time: datetime
    initial_price: float
    
    # @field_validator('start_time', mode="after")
    # def parse_start_date(cls, value):
    #     return parse(value)
    
    # @field_validator('end_time', mode="after")
    # def parse_end_date(cls, value):
    #     return parse(value)

class AuctionGetorDelete(BaseModel):
    id: Optional[int]
    good_id: Optional[int]


class Auction(BaseModel):
    id: int
    description: str
    start_time: datetime
    end_time: datetime
    closed: Optional[bool] = False
    initial_price: float
    sold_price: Optional[float]
    good_id: int
    winner_id: Optional[int]

    # @field_validator('start_time', mode="after")
    # def parse_start_date(cls, value):
    #     return parse(value)
    
    # @field_validator('end_time', mode="after")
    # def parse_end_date(cls, value):
    #     return parse(value)

    class Config:
        orm_mode = True
