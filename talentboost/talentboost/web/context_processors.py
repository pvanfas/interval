from main.forms import SchoolForm, StudentRegistrationForm

from .models import FAQ, Achievement, Feature, News, Project, Setting, Winner


def main_context(request):
    return {
        "domain": request.META["HTTP_HOST"],
        "achievements": Achievement.objects.all(),
        "newses": News.objects.all(),
        "winners": Winner.objects.all(),
        "projects": Project.objects.all(),
        "features": Feature.objects.all(),
        "faqs": FAQ.objects.all(),
        "registration_form": StudentRegistrationForm(),
        "school_form": SchoolForm(),
        "settings": Setting.objects.first(),
    }
