import json

import requests

from web.models import DemoRequest

obj = DemoRequest.objects.all().last()


def run():
    API_HOST = "https://api-in21.leadsquared.com/v2/"
    ACCESS_KEY = "u$r75c773c740ea81296419c8386f74a742"
    SECRET_KEY = "0f82018e5aa3aba420a3b3f2cf442e070b9af918"
    CRM_HOST = f"{API_HOST}LeadManagement.svc/Lead.Create?accessKey={ACCESS_KEY}&secretKey={SECRET_KEY}"
    payload = json.dumps(
        [
            {"Attribute": "mx_Filled_by", "Value": obj.raised_by},
            {"Attribute": "FirstName", "Value": obj.student_name},
            {"Attribute": "EmailAddress", "Value": obj.email},
            {"Attribute": "Mobile", "Value": obj.phone_number},
            {"Attribute": "mx_Whatsapp", "Value": obj.whatsapp_number},
            {"Attribute": "mx_sub_class", "Value": obj.standard},
            {"Attribute": "mx_Country", "Value": obj.country.name},
            {"Attribute": "mx_Message", "Value": ""},
            {"Attribute": "mx_Lead_Status", "Value": "Pending"},
            {"Attribute": "mx_Form_Name", "Value": "Popup"},
        ]
    )
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.request("POST", CRM_HOST, headers=headers, data=payload)
    print(response.text)
    return response.text
