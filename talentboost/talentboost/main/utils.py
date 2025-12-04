import json

import requests
from django.conf import settings
from main.models import StudentRegistration


def send_whatsapp_message(student):
    variable_2 = student.register_number
    whatsapp_number = str(int(student.whatsapp_number))
    # print("Sending WhatsApp message", student.name, whatsapp_number, variable_2)
    url = settings.WHATSAAP_API_URL
    payload = json.dumps(
        {
            "channelId": settings.WHATSAPP_CHANNEL_ID,
            "channelType": "whatsapp",
            "recipient": {"name": student.name, "phone": whatsapp_number},
            "whatsapp": {
                "type": "template",
                "template": {
                    "templateName": "registration_msg2_",
                    "bodyValues": {"name": student.name, "variable_2": variable_2},
                },
            },
        }
    )
    print(payload)
    headers = {
        "apiKey": settings.WHATSAPP_API_KEY,
        "apiSecret": settings.WHATSAPP_API_SECRET,
        "Content-Type": "application/json",
    }
    student.is_message_sent = True
    student.save()

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        student.is_message_sent = True
        student.save()
    except Exception as e:
        print("Error in sending WhatsApp message", e)
        return False


def send_bulk_whatsapp_message(item):
    students_pks = json.loads(item.success_data)
    students = StudentRegistration.objects.filter(pk__in=students_pks)
    for student in students:
        send_whatsapp_message(student)
