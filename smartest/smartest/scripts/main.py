import uuid

from main.models import Standard, Student
from users.models import CustomUser as User


def run():
    print("Hello, World!")
    standard_id = "baba45bb-c7ae-4112-b049-20ec728a5fc0"
    student_names = ["Ashwin Vijayan", "Neha Soman", "Meera Mohan", "Sarath Chandra", "Akshay Unnikrishnan", "Vishnu Dev", "Revathy Pillai"]
    for i in range(len(student_names)):
        first_name, last_name = student_names[i].split()
        username = f"{first_name.lower()}"
        email = f"{first_name.lower()}.{last_name.lower()}@school.com"
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password="Test@123",
                first_name=first_name,
                last_name=last_name,
                usertype="Student",
            )
            standard = Standard.objects.get(id=uuid.UUID(standard_id))
            student = Student.objects.create(user=user, standard=standard)
            print(f"Created student: {student}")
        except Exception as e:
            print(f"Error: {e}")
