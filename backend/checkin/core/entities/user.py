from dataclasses import dataclass, field
from typing import Optional
import uuid


@dataclass 
class User:
    first_name : str 
    last_name : str 
    email : str 
    password : str
    id: Optional[int] = field(default=None)
    