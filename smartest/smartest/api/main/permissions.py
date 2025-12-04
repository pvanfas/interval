from rest_framework.permissions import IsAuthenticated


class IsAdministrator(IsAuthenticated):
    """
    Allows access only to users with usertype 'Administrator'.
    """

    def has_permission(self, request, view):
        is_authenticated = super().has_permission(request, view)
        return is_authenticated and request.user.usertype == "Administrator"


class IsTeacher(IsAuthenticated):
    """
    Allows access only to users with usertype 'Teacher'.
    """

    def has_permission(self, request, view):
        is_authenticated = super().has_permission(request, view)
        return is_authenticated and request.user.usertype == "Teacher"


class IsStudent(IsAuthenticated):
    """
    Allows access only to users with usertype 'Student'.
    """

    def has_permission(self, request, view):
        is_authenticated = super().has_permission(request, view)
        return is_authenticated and request.user.usertype == "Student"


class IsStudentOrTeacher(IsAuthenticated):
    """
    Allows access only to users with usertype 'Student' or 'Teacher'.
    """

    def has_permission(self, request, view):
        is_authenticated = super().has_permission(request, view)
        return is_authenticated and request.user.usertype in ["Student", "Teacher"]
