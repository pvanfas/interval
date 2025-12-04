from django.db import models
from django.urls import reverse


class IndustryExpert(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="industry_expert_logo")
    priority = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ("priority",)
        verbose_name = "Industry Expert"
        verbose_name_plural = "Industry Experts"

    def __str__(self):
        return self.name


class SkillCategory(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    icon = models.FileField(upload_to="skill_category_icon")

    class Meta:
        verbose_name = "Skill Category"
        verbose_name_plural = "Skill Categories"

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    summary = models.TextField()
    image = models.ImageField(upload_to="course_image")
    skill_category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("web:program_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ("title",)
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to="testimonial_image")
    content = models.TextField()

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return self.name


class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question


class Speaker(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to="speaker_image")

    class Meta:
        verbose_name = "Speaker"
        verbose_name_plural = "Speakers"

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="event_image")
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    speaker = models.ForeignKey("Speaker", on_delete=models.CASCADE)
    registration_link = models.URLField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ("-date",)
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.title


class PhoneRequest(models.Model):
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Phone Request"
        verbose_name_plural = "Phone Requests"

    def __str__(self):
        return self.phone


class ChatRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Chat Request"
        verbose_name_plural = "Chat Requests"

    def __str__(self):
        return self.name


class Application(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    interests = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Application"
        verbose_name_plural = "Applications"

    def __str__(self):
        return self.name


class CourseEnquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20)
    course = models.ForeignKey("Course", on_delete=models.CASCADE)
    message = models.TextField("Why do you want to join this course?")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Course Enquiry"
        verbose_name_plural = "Course Enquiries"

    def __str__(self):
        return self.name
