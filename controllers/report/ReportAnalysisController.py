from db_model.MASTER_MODEL import insert_data,custom_select_sql_query,select_one_data,select_data
from utils.first_day_last_day import first_day_last_day,first_year_day_last_year_day
# from Library.DecimalEncoder import DecimalEncoder
# import json

@staticmethod
async def energy_usage_billing(user_data,params):
    try:
        if user_data['user_type'] == "C":
            if params.report_type == "M": # monthly
                fdatetdate=first_day_last_day(params.start_date_time)
                print("??????????????-----------------???????",fdatetdate["first_day"])
                condition = f"ed.client_id = {user_data['client_id']} AND ed.device_id = {params.device_id}"
                select="ed.e1,ed.e2,ed.e3,ed.energy_data_id, ed.device_id, ed.do_channel, ed.activep1, ed.activep2, ed.activep3, ed.apparentp1, ed.apparentp2, ed.apparentp3, ed.pf1, ed.pf2, ed.pf3, DATE_FORMAT(ed.date, '%Y-%m-%d') AS date, TIME_FORMAT(ed.time, '%H:%i:%s') AS time"
                table=f"""td_energy_data AS ed
                                INNER JOIN (
                                    SELECT
                                        date,
                                        MAX(time) AS max_time
                                    FROM
                                        td_energy_data
                                    WHERE
                                        client_id = {user_data['client_id']} AND device_id = {params.device_id}
                                        AND date BETWEEN '{fdatetdate["first_day"]}' AND '{fdatetdate["last_day"]}'
                                    GROUP BY
                                        date
                                ) AS sub_ed ON ed.date = sub_ed.date AND ed.time = sub_ed.max_time"""
                data = select_data(table,select, condition)
                # data = select_data(table,select, condition,order_by="ed.date DESC, ed.time DESC")
                # if params.end_date_time == None:
                    #     condition=f"a.client_id={user_data['client_id']} AND a.device_id={params.device_id} AND a.date BETWEEN '{params.start_date_time}' AND '{params.start_date_time}'"
                    # condition=f"a.client_id={user_data['client_id']} AND a.device_id={params.device_id} AND a.date BETWEEN '{params.start_date_time}' AND '{params.end_date_time}'"
            elif params.report_type == "Y":  #yearly
                fdatetdate=first_year_day_last_year_day(params.start_date_time)
                condition = f"ed.client_id = {user_data['client_id']} AND ed.device_id = {params.device_id}"
                select=f""" ed.energy_data_id,
                            ed.device_id,
                            ed.do_channel,
                            ed .e1,
                            ed .e2,
                            ed .e3,
                            DATE_FORMAT(ed.date, '%Y-%m-%d') AS DATE,
                            TIME_FORMAT(ed.time, '%H:%i:%s') AS TIME"""
                            
                table =f""" td_energy_data AS ed
                                INNER JOIN(
                                    SELECT
                                        MAX(energy_data_id) AS max_energy_data_id,
                                        YEAR(DATE) AS YEAR,
                                        MONTH(DATE) AS MONTH
                                    FROM
                                        td_energy_data
                                    WHERE
                                        client_id = 1 AND device_id = 1
                                        AND date BETWEEN '{fdatetdate["first_day"]}' AND '{fdatetdate["last_day"]}'
                                    GROUP BY
                                        YEAR(DATE),
                                        MONTH(DATE)
                                ) AS sub_ed
                                ON
                                ed.energy_data_id = sub_ed.max_energy_data_id """
                data = select_data(table,select, condition,order_by="ed.date DESC, ed.time DESC")
            elif params.report_type == "C": # customized
                condition = f"ed.client_id = {user_data['client_id']} AND ed.device_id = {params.device_id}"
                select="ed.e1,ed.e2,ed.e3,ed.energy_data_id, ed.device_id, ed.do_channel, ed.activep1, ed.activep2, ed.activep3, ed.apparentp1, ed.apparentp2, ed.apparentp3, ed.pf1, ed.pf2, ed.pf3, DATE_FORMAT(ed.date, '%Y-%m-%d') AS date, TIME_FORMAT(ed.time, '%H:%i:%s') AS time"
                table=f"""td_energy_data AS ed
                                INNER JOIN (
                                    SELECT
                                        date,
                                        MAX(time) AS max_time
                                    FROM
                                        td_energy_data
                                    WHERE
                                        client_id = {user_data['client_id']} AND device_id = {params.device_id}
                                        AND date BETWEEN '{params.start_date_time}' AND '{params.end_date_time}'
                                    GROUP BY
                                        date
                                ) AS sub_ed ON ed.date = sub_ed.date AND ed.time = sub_ed.max_time"""
                data = select_data(table,select, condition)
        elif user_data['user_type'] == "U" or user_data['user_type'] == "O":
          print("fxgbxd")
          
        condition_bill = f"a.organization_id=b.organization_id AND a.client_id = {user_data['client_id']} AND b.client_id={user_data['client_id']} AND a.device_id = {params.device_id}"
        select_bill = "b.*"
        master_bill = select_data("md_manage_user_device AS a,md_billing_organization AS b",select_bill, condition_bill)
        return {"data":data , "master_bill":master_bill}
    except Exception as e:
        return ValueError("Error in energy_usage_billing",e)
        
    