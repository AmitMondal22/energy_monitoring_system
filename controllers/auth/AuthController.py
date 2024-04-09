from db_model.MASTER_MODEL import select_data, insert_data,select_one_data
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
        user_info=select_one_data("users",select,condition,None)

        if user_info is None:
            raise ValueError("User login failed")
        else:
            
            if user_info['user_type'] == 'S':
                table="users"
                select="user_id, user_name, user_email, user_info_id, user_active_status, user_type, otp_number, otp_active_status, password, created_by, DATE_FORMAT(created_at, '%Y-%m-%d %H:%i:%s') AS created_at"
                condition=f"user_email = '{user.email}'"
                order_by=None
                login_data=select_one_data(table,select,condition,order_by)    
                print("zdhcsdjkd",)
            elif user_info['user_type'] == 'A':
                print("zdhcsdjkd",)
            elif user_info['user_type'] == 'C':
                table="users AS u,  md_client AS c"
                select="u.user_id, u.user_name, u.user_email, u.user_info_id, u.user_active_status, u.user_type, u.otp_number, u.otp_active_status, u.password, u.created_by, c.client_id, c.client_name, c.client_address, c.client_mobile, c.client_email"
                condition=f"u.user_email = '{user.email}' AND u.user_info_id = c.client_id AND u.user_active_status = 'Y' AND u.user_type = 'C'"
                order_by=None
                login_data=select_one_data(table,select,condition,order_by) 
                print(login_data["password"])
            elif user_info['user_type'] == 'O':
                print("zdhcsdjkd",)
            elif user_info['user_type'] == 'U':
                print("zdhcsdjkd",)
            else:
                raise ValueError("Invalid user type")
            
            
                
            
            
            
            
            if verify_password(user.password, login_data["password"]) is False:
                raise ValueError("Password mismatch")
            else:
                # Create and return JWT token
                access_token = create_access_token(data={"sub": login_data})
                print("Access token created",access_token)
                
                
            return {"user_data":login_data,"token":access_token}
    
    
    except Exception as e:
        raise e
