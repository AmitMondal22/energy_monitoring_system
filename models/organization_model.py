from pydantic import BaseModel, Field, constr, validator
from datetime import date

class AddOrganization(BaseModel):
    organization_name: str
    created_by: int


class EditOrganization(BaseModel):
    organization_id: int
    organization_name: str
    created_by: int
    
class DeleteOrganization(BaseModel):
    organization_id: int
    # created_by: int