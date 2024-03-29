from db_model.MASTER_MODEL import select_data, insert_data
from utils.has_password import get_password_hash, verify_password
from utils.otp import generate_otp
from utils.date_time_format import get_current_datetime
from utils.jwt_access import create_access_token



@staticmethod
async def register(user) -> dict:
    try:
        password = get_password_hash(user.password)
        new_otp = generate_otp(6)
        current_datetime = get_current_datetime()
        columns = "user_name, user_email, user_info_id, user_active_status, user_type, otp_number, otp_active_status, password, created_by, created_at"
        value = f"'{user.name}', '{user.email}', 1, 'Y', '{user.user_type}', {new_otp}, 'N', '{password}', 0, '{current_datetime}'"
        user_id = insert_data("users", columns, value)
        if user_id is None:
            raise ValueError("User registration failed")
        else:
            user_data = {"user_id": user_id, "name": user.name, "email": user.email}
            print("User registration successful",user_data)
        return user_data
    except Exception as e:
        raise e


@staticmethod
async def login(user) -> dict:
    try:
        condition = f"user_email = '{user.email}'"
        select = f"user_id, user_name, user_email, user_info_id, user_active_status, user_type, otp_number, otp_active_status, password, created_by, DATE_FORMAT(created_at, '%Y-%m-%d %H:%i:%s') AS created_at"
        user_data=select_data("users",select,None)
        if user_data is None:
            raise ValueError("User login failed")
        else:
            if verify_password(user.password, user_data[0]['password']) is False:
                raise ValueError("User login failed")
            else:
                # Create and return JWT token
                access_token = create_access_token(data={"sub": user_data})
                print("Access token created",access_token)
                
                
            return {"user_data":user_data,"token":access_token}
    
    
    except Exception as e:
        raise e
