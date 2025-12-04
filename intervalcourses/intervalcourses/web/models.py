from django.db import models

PROGRAM_TYPE_CHOICES = (
    ("CLUB", "Club Courses"),
    ("NON_ACADEMIC", "Non Academic Courses"),
)
CLASS_CHOICES = (
    ("1", "Class 1"),
    ("2", "Class 2"),
    ("3", "Class 3"),
    ("4", "Class 4"),
    ("5", "Class 5"),
    ("6", "Class 6"),
    ("7", "Class 7"),
    ("8", "Class 8"),
    ("9", "Class 9"),
    ("10", "Class 10"),
    ("11", "Class 11"),
    ("12", "Class 12"),
)
MEDIA_CHOICES = (
    ("bi-instagram", "Instagram"),
    ("bi-facebook", "Facebook"),
    ("bi-youtube", "Youtube"),
    ("bi-pinterest", "Pinterest"),
    ("bi-twitter", "Twitter"),
    ("bi-threads", "Threads"),
    ("bi-tiktok", "Tiktok"),
    ("bi-wikipedia", "Wikipedia"),
    ("bi-google", "Google"),
    ("bi-google-play", "Google Play"),
    ("bi-github", "github"),
    ("bi-xbox", "X Box"),
    ("bi-linkedin", "Linkedin"),
    ("bi-youtube", "Youtube"),
)
AGEGROUP_CHOICES = (
    ("3-5", "3-5 Years"),
    ("6-9", "6-9 Years"),
    ("10-13", "10-13 Years"),
    ("14-18", "14-18 Years"),
    ("18-20", "18-20 Years"),
    ("20P", "20 Plus Years"),
)

KEY_CHOICES = (
    ("home_meta_title", "Home Page Meta Title"),
    ("home_meta_desc", "Home Page Meta Description"),
    ("littlegenie_meta_title", "Little Genie Page Meta Title"),
    ("littlegenie_meta_desc", "Little Genie Page Meta Description"),
    ("foundation_meta_title", "Foundation Page Meta Title"),
    ("foundation_meta_desc", "Foundation Page Meta Description"),
)


class Slider(models.Model):
    title = models.CharField("Student Name", max_length=200)
    subject = models.CharField("Subject", max_length=200)
    image = models.ImageField(upload_to="slider/")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to="testimonial/")
    content = models.TextField()
    video_id = models.CharField(max_length=11)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return self.name


class FDEnquiry(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField("Phone Number", max_length=25)
    whatsapp_number = models.CharField("WhatsApp Number", max_length=25)
    standard = models.CharField("Standard", max_length=10, choices=CLASS_CHOICES)

    timestamp = models.DateTimeField(auto_now_add=True)
    # Fields for UTM parameters
    utm_source = models.CharField(max_length=255, blank=True, null=True)
    utm_medium = models.CharField(max_length=255, blank=True, null=True)
    utm_campaign = models.CharField(max_length=255, blank=True, null=True)
    utm_content = models.CharField(max_length=255, blank=True, null=True)
    utm_term = models.CharField(max_length=255, blank=True, null=True)

    is_sent2crm = models.BooleanField(default=False)
    lsq_status_code = models.IntegerField(blank=True, null=True)
    lsq_status = models.CharField(max_length=200, blank=True, null=True)
    lsq_exception_type = models.TextField(blank=True, null=True)
    lsq_exception_message = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Enquiry"
        verbose_name_plural = "Enquiries"

    def __str__(self):
        return self.name


class LGEnquiry(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField("Phone Number", max_length=25)
    whatsapp_number = models.CharField("WhatsApp Number", max_length=25)
    age = models.PositiveSmallIntegerField("Age")

    timestamp = models.DateTimeField(auto_now_add=True)
    # Fields for UTM parameters
    utm_source = models.CharField(max_length=255, blank=True, null=True)
    utm_medium = models.CharField(max_length=255, blank=True, null=True)
    utm_campaign = models.CharField(max_length=255, blank=True, null=True)
    utm_content = models.CharField(max_length=255, blank=True, null=True)
    utm_term = models.CharField(max_length=255, blank=True, null=True)

    is_sent2crm = models.BooleanField(default=False)
    lsq_status_code = models.IntegerField(blank=True, null=True)
    lsq_status = models.CharField(max_length=200, blank=True, null=True)
    lsq_exception_type = models.TextField(blank=True, null=True)
    lsq_exception_message = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Enquiry"
        verbose_name_plural = "Enquiries"

    def __str__(self):
        return self.name


class Configuration(models.Model):
    key = models.CharField(max_length=200, unique=True, choices=KEY_CHOICES)
    value = models.TextField()

    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configurations"

    def __str__(self):
        return self.key
