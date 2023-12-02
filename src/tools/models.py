from pydantic import BaseModel, ConfigDict
from typing import Optional, Union
import json


class Car(BaseModel):
    model_config = ConfigDict(
        protected_namespaces=('protect_me_', 'also_protect_')
    )

    car_id: Optional[int] = None
    man_id: Optional[int] = None
    model_id: Optional[int] = None
    prod_year: Optional[int] = None
    price_usd: Optional[Union[int, float]] = None
    price_value: Optional[Union[int, float]] = None
    fuel_type_id: Optional[int] = None
    gear_type_id: Optional[int] = None
