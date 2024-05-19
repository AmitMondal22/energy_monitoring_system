from db_model.MASTER_MODEL import insert_data,custom_select_sql_query,select_one_data,select_data


@staticmethod
async def energy_usage_billing(user_data,params):
    try:
        if user_data['user_type'] == "C":
            if params.report_type == "M":
                if params.end_date_time == None:
                    condition=f"a.client_id={user_data['client_id']} AND a.device_id={params.device_id} AND a.date BETWEEN '{params.start_date_time}' AND '{params.start_date_time}'"
                condition=f"a.client_id={user_data['client_id']} AND a.device_id={params.device_id} AND a.date BETWEEN '{params.start_date_time}' AND '{params.end_date_time}'"
            elif params.report_type == "Y":
                condition=f"a.client_id={user_data['client_id']} AND a.device_id={params.device_id} AND a.date BETWEEN '{params.start_date_time}' AND '{params.end_date_time}'"
            elif params.report_type == "C":
                condition=f"a.client_id={user_data['client_id']} AND a.device_id={params.device_id} AND a.date BETWEEN '{params.start_date_time}' AND '{params.end_date_time}'"
            select = "a.e1,a.e2,a.e3,a.date,a.time"
            table="td_energy_data AS a"
  
            
            
        elif user_data['user_type'] == "U" or user_data['user_type'] == "O":
            if params.report_type == "M":
                condition=f"a.client_id={user_data['client_id']} AND a.device_id={params.device_id} AND a.date BETWEEN '{params.start_date_time}' AND '{params.end_date_time}'"
            elif params.report_type == "Y":
                condition=f"a.client_id={user_data['client_id']} AND a.device_id={params.device_id} AND a.date BETWEEN '{params.start_date_time}' AND '{params.end_date_time}'"
            elif params.report_type == "C":
                condition=f"a.client_id={user_data['client_id']} AND a.device_id={params.device_id} AND a.date BETWEEN '{params.start_date_time}' AND '{params.end_date_time}'"
                
                
            select = "a.e1,a.e2,a.e3,a.date,a.time"
            table="td_energy_data AS a"
        data_list=select_data(table,select,condition)
        return data_list
    except Exception as e:
        return ValueError("Error in energy_usage_billing",e)
        
    