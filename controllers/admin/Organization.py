
from db_model.MASTER_MODEL import select_data, insert_data,update_data,delete_data
from utils.date_time_format import get_current_datetime

@staticmethod
def add_organization(organization):
    try:
              
        current_datetime = get_current_datetime()
        columns = "organization_name, created_by, created_at"
        value = f"'{organization.organization_name}', {organization.created_by},'{current_datetime}'"
        organization_id = insert_data("md_organization", columns, value)
        if organization_id is None:
            raise ValueError("organization registration failed")
        else:
            user_data = {"user_id": organization_id, "organization_name": organization.organization_name, "created_by": organization.created_by}
            print("User registration successful",user_data)
        return user_data
    except Exception as e:
        raise e
    
@staticmethod
def list_organization():
    try:
        select="organization_id, organization_name, created_by, DATE_FORMAT(created_at, '%Y-%m-%d %H:%i:%s') AS created_at"
        data = select_data("md_organization", select)
        return data
    except Exception as e:
        raise e
    
    
@staticmethod
def edit_organization(organization):
    try:
        condition = f"organization_id = {organization.organization_id}"
        columns={"organization_name":organization.organization_name,"created_by":organization.created_by,"updated_at":get_current_datetime()}
        data = update_data("md_organization", columns, condition)
        return data
    except Exception as e:
        raise e

@staticmethod
def delete_organization(organization):
    try:
        condition = f"organization_id = {organization.organization_id}"
        data = delete_data("md_organization", condition)
        return data
    except Exception as e:
        raise e