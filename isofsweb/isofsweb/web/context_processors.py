from .forms import ApplicationForm, ChatRequestForm, PhoneRequestForm


def main_context(request):
    return {
        "domain": request.META["HTTP_HOST"],
        "phone_request_form": PhoneRequestForm(),
        "chat_request_form": ChatRequestForm(),
        "admission_form": ApplicationForm(),
    }
