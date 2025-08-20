from dataclasses import dataclass 

@dataclass 
class Administrator:
    first_name : str 
    last_name : str
    email : str
    password : str
    permission : list[str] 
