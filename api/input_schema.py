from pydantic import BaseModel, Field
from typing import Literal


class InsuranceInput(BaseModel):
    Gender: Literal['Male', 'Female']
    Age: int = Field(..., ge=18, le=100)
    Driving_License: Literal[0, 1]
    Region_Code: float
    Previously_Insured: Literal[0, 1]
    Vehicle_Age: Literal['< 1 Year', '1-2 Year', '> 2 Years']
    Vehicle_Damage: Literal['Yes', 'No']
    Annual_Premium: float = Field(..., gt=0)
    Policy_Sales_Channel: float
    Vintage: int = Field(..., ge=0)

    class Config:
        schema_extra = {
            "example": {
                "Gender": "Male",
                "Age": 35,
                "Driving_License": 1,
                "Region_Code": 28.0,
                "Previously_Insured": 0,
                "Vehicle_Age": "> 2 Years",
                "Vehicle_Damage": "Yes",
                "Annual_Premium": 35000.0,
                "Policy_Sales_Channel": 152.0,
                "Vintage": 120
            }
        }
