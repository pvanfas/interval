from import_export import resources

from .models import StudentRegistration


class StudentRegistrationResource(resources.ModelResource):
    class Meta:
        model = StudentRegistration
