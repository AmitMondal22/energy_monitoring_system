from db_model.MASTER_MODEL import insert_data,custom_select_sql_query,select_one_data,select_data,update_data
from utils.date_time_format import get_current_datetime

async def client_screen_settings(user, params):
    try:
        data = select_data("st_view_organization", "*", f"client_id = {user['client_id']} AND organization_id = {params.organization_id}")
        return data
    except Exception as e:
        raise e

async def client_screen_settings_edit(user, params):
    try:
        current_datetime = get_current_datetime()
        if params.id_view_organization:
            table="st_view_organization"
            set_value=f"gv_energy_used = '{params.gv_energy_used}', gv_voltage = '{params.gv_voltage}', gv_current = '{params.gv_current}', gv_power = '{params.gv_power}', mn_add_organization = '{params.mn_add_organization}', mn_device_management = '{params.mn_device_management}', mn_user_management = '{params.mn_user_management}', en_tab_device_info = '{params.en_tab_device_info}', en_tab_create_alert = '{params.en_tab_create_alert}', en_tab_scheduling = '{params.en_tab_scheduling}', en_tab_report_analysi = '{params.en_tab_report_analysi}', updated_at='{current_datetime}' "
            condition=f"id_view_organization = {params.id_view_organization} AND client_id = {user['client_id']} AND organization_id = {params.organization_id}"
            data=update_data(table, set_value, condition)
        else:
            table="st_view_organization"
            columns="user_type, client_id, organization_id, gv_energy_used, gv_voltage, gv_current, gv_power, mn_add_organization, mn_device_management, mn_user_management, en_tab_device_info, en_tab_create_alert, en_tab_scheduling, en_tab_report_analysi, created_by, created_at, updated_at"
            
            values=f"{params.user_type ,user['client_id']}, {params.organization_id}, '{params.gv_energy_used}', '{params.gv_voltage}', '{params.gv_current}', '{params.gv_power}', '{params.mn_add_organization}', '{params.mn_device_management}', '{params.mn_user_management}', '{params.en_tab_device_info}', '{params.en_tab_create_alert}', '{params.en_tab_scheduling}', '{params.en_tab_report_analysi}', {user['user_id']},'{current_datetime}','{current_datetime}'"
            data=insert_data(table, columns, values)
            
            
            
            
        data = select_one_data("st_view_organization", "*", f"client_id = {user['client_id']} AND organization_id = {params.organization_id}")
        return data
    except Exception as e:
        raise e