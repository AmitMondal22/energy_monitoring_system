from db_model.MASTER_MODEL import insert_data,custom_select_sql_query,select_one_data,select_data
from utils.first_day_last_day import first_day_last_day

@staticmethod
async def energy_usage_billing(user_data,params):
    try:
        if user_data['user_type'] == "C":
            if params.report_type == "M": # monthly
                print(first_day_last_day(params.start_date_time))
                condition = f"ed.client_id = {user_data['client_id']} AND ed.device_id = {params.device_id}"
                select="ed.energy_data_id, ed.device_id, ed.do_channel, ed.activep1, ed.activep2, ed.activep3, ed.apparentp1, ed.apparentp2, ed.apparentp3, ed.pf1, ed.pf2, ed.pf3, DATE_FORMAT(ed.date, '%Y-%m-%d') AS date, TIME_FORMAT(ed.time, '%H:%i:%s') AS time"
                table=f"""td_energy_data AS ed
                                INNER JOIN (
                                    SELECT
                                        date,
                                        MAX(time) AS max_time
                                    FROM
                                        td_energy_data
                                    WHERE
                                        client_id = {user_data['client_id']} AND device_id = {params.device_id}
                                        AND date BETWEEN DATE_SUB(CURDATE(), INTERVAL 30 DAY) AND CURDATE()
                                    GROUP BY
                                        date
                                ) AS sub_ed ON ed.date = sub_ed.date AND ed.time = sub_ed.max_time"""
                data = select_data(table,select, condition,order_by="date DESC, time DESC")
            
            
            
                if params.end_date_time == None:
                    condition=f"a.client_id={user_data['client_id']} AND a.device_id={params.device_id} AND a.date BETWEEN '{params.start_date_time}' AND '{params.start_date_time}'"
                condition=f"a.client_id={user_data['client_id']} AND a.device_id={params.device_id} AND a.date BETWEEN '{params.start_date_time}' AND '{params.end_date_time}'"
            elif params.report_type == "Y":  #yearly
                
                
                condition = f"ed.client_id = {user_data['client_id']} AND ed.device_id = {params.device_id}"
                select="ed.energy_data_id, ed.device_id, ed.do_channel, ed.activep1, ed.activep2, ed.activep3, ed.apparentp1, ed.apparentp2, ed.apparentp3, ed.pf1, ed.pf2, ed.pf3, DATE_FORMAT(ed.date, '%Y-%m-%d') AS date, TIME_FORMAT(ed.time, '%H:%i:%s') AS time "
                table =f"td_energy_data AS ed INNER JOIN (SELECT  MAX(energy_data_id) AS max_energy_data_id,  YEAR(date) AS year, MONTH(date) AS month FROM td_energy_data WHERE client_id = {user_data['client_id']} AND device_id = {params.device_id} GROUP BY  YEAR(date), MONTH(date) ) AS sub_ed ON ed.energy_data_id = sub_ed.max_energy_data_id"
                data = select_data(table,select, condition,order_by="ed.date DESC, ed.time DESC")
                
                
                
                condition=f"a.client_id={user_data['client_id']} AND a.device_id={params.device_id} AND a.date BETWEEN '{params.start_date_time}' AND '{params.end_date_time}'"
            elif params.report_type == "C": # customize
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
        
    