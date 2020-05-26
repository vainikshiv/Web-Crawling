import requests
import json
from db import Insert_into_table, Fetch_data

class Scrap:

    #Login Method and get token
    def login():
        data = {
            "login_id": "triose",
            "password": "triose123"
        }
        global header
        header = {}
        response = requests.post("http://3.6.0.2/inject-solar-angular/inject_solar_server/admin/Admin/login", data=json.dumps(data))
        
        # Get the token
        header["Authorization"] = response.json()["resultObject"]["token"]
        return response.status_code 

    # Get the error data method
    def get_error():
        d = {"user_id": "90", "start_date": "2020-01-01", "end_date": "2020-02-29", "limit": 90, "offset": 0}
        res = requests.get("http://3.6.0.2/inject-solar-angular/inject_solar_server/normal/Alarms/getClearedNormalAlarms",data=json.dumps(d), headers=header)
        l = []
        for i in res.json()["resultObject"]:
            l.append((i["dev_name"], i["name"],i["alarm_id"],i['date_time'],i["clear_time"],i["alarm_msg"]))
        Insert_into_table(l)
        return "Data inserted"

#get the instance of class
print(Scrap.login())
print(Scrap.get_error())
# Fetch_data("errors")  # Shows the error table data