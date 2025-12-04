import json

import requests

API_HOST = "https://api-in21.leadsquared.com/v2/"
ACCESS_KEY = "u$r75c773c740ea81296419c8386f74a742"
SECRET_KEY = "0f82018e5aa3aba420a3b3f2cf442e070b9af918"
CRM_HOST = f"{API_HOST}LeadManagement.svc/Lead.Capture?accessKey={ACCESS_KEY}&secretKey={SECRET_KEY}"


def send_demorequest_to_crm(obj):
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
            {"Attribute": "mx_Lead_Status", "Value": "Not Qualified"},
            {"Attribute": "mx_Field_1_Sources", "Value": "Digital Marketing"},
            {"Attribute": "mx_Field_2_Sources", "Value": "Website"},
            {"Attribute": "mx_Web_Lead_Id", "Value": str(obj.token)},
            {"Attribute": "SourceCampaign", "Value": obj.utm_source},
            {"Attribute": "SourceMedium", "Value": obj.utm_medium},
            {"Attribute": "mx_UTM_Campaign", "Value": obj.utm_campaign},
            {"Attribute": "SourceContent", "Value": obj.utm_content},
            {"Attribute": "mx_UTM_Term", "Value": obj.utm_term},
            {"Attribute": "mx_Form_Name", "Value": "DemoPopup"},
        ]
    )
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.request("POST", CRM_HOST, headers=headers, data=payload)
    print("Response from CRM:", response.text)
    print("Status Code:", response.status_code)
    obj.lsq_status_code = response.status_code
    obj.lsq_status = response.json().get("Status")
    if response.status_code == 200:
        obj.lsq_exception_type = None
        obj.lsq_exception_message = None
    else:
        obj.lsq_exception_type = response.json().get("ExceptionType")
        obj.lsq_exception_message = response.json().get("ExceptionMessage")
    obj.save()
    return response.text


def send_lead_to_crm(obj):
    payload = json.dumps(
        [
            {"Attribute": "mx_Filled_by", "Value": ""},
            {"Attribute": "FirstName", "Value": obj.name},
            {"Attribute": "mx_Country", "Value": obj.country.name},
            {"Attribute": "EmailAddress", "Value": obj.email},
            {"Attribute": "Mobile", "Value": obj.phone_number},
            {"Attribute": "mx_Whatsapp", "Value": obj.whatsapp_number},
            {"Attribute": "mx_Message", "Value": obj.purpose.name if obj.purpose else ""},
            {"Attribute": "mx_sub_class", "Value": ""},
            {"Attribute": "mx_Lead_Status", "Value": "Not Qualified"},
            {"Attribute": "mx_Field_1_Sources", "Value": "Digital Marketing"},
            {"Attribute": "mx_Field_2_Sources", "Value": "Website"},
            {"Attribute": "mx_Web_Lead_Id", "Value": str(obj.token)},
            {"Attribute": "SourceCampaign", "Value": obj.utm_source},
            {"Attribute": "SourceMedium", "Value": obj.utm_medium},
            {"Attribute": "mx_UTM_Campaign", "Value": obj.utm_campaign},
            {"Attribute": "SourceContent", "Value": obj.utm_content},
            {"Attribute": "mx_UTM_Term", "Value": obj.utm_term},
            {"Attribute": "mx_Form_Name", "Value": "Popup"},
        ]
    )
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.request("POST", CRM_HOST, headers=headers, data=payload)
    print("Response from CRM:", response.text)
    print("Status Code:", response.status_code)
    obj.lsq_status_code = response.status_code
    obj.lsq_status = response.json().get("Status")
    if response.status_code == 200:
        obj.lsq_exception_type = None
        obj.lsq_exception_message = None
    else:
        obj.lsq_exception_type = response.json().get("ExceptionType")
        obj.lsq_exception_message = response.json().get("ExceptionMessage")
    obj.save()
    return response.text
