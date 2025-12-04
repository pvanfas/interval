import uuid

from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField
from taggit.managers import TaggableManager
from django.utils.html import strip_tags
from django.core.files.images import get_image_dimensions


PROGRAM_TYPE_CHOICES = (
    ("CLUB", "Club Courses"),
    ("NON_ACADEMIC", "Non Academic Courses"),
)
CLASS_CHOICES = (
    ("LKG", "LKG"),
    ("UKG", "UKG"),
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
    ("about_meta_title", "About Page Meta Title"),
    ("about_meta_desc", "About Page Meta Description"),
    ("blogs_meta_title", "Blogs Page Meta Title"),
    ("blogs_meta_desc", "Blogs Page Meta Description"),
    ("boards_meta_title", "Boards Page Meta Title"),
    ("boards_meta_desc", "Boards Page Meta Description"),
    ("clubs_meta_title", "Clubs Page Meta Title"),
    ("clubs_meta_desc", "Clubs Page Meta Description"),
    ("news_meta_title", "News Page Meta Title"),
    ("news_meta_desc", "News Page Meta Description"),
    ("nonacademics_meta_title", "Nonacademics Page Meta Title"),
    ("nonacademics_meta_desc", "Nonacademics Page Meta Description"),
    ("subjects_meta_title", "Subjects Page Meta Title"),
    ("subjects_meta_desc", "Subjects Page Meta Description"),
    ("testimonials_meta_title", "Testimonials Page Meta Title"),
    ("testimonials_meta_desc", "Testimonials Page Meta Description"),
    ("contact_meta_title", "Contact Page Meta Title"),
    ("contact_meta_desc", "Contact Page Meta Description"),
    ("countries_meta_title", "Countries Page Meta Title"),
    ("countries_meta_desc", "Countries Page Meta Description"),
    ("courses_meta_title", "Courses Page Meta Title"),
    ("courses_meta_desc", "Courses Page Meta Description"),
    ("downloads_meta_title", "Downloads Page Meta Title"),
    ("downloads_meta_desc", "Downloads Page Meta Description"),
    ("tools_meta_title", "Tools Page Meta Title"),
    ("tools_meta_desc", "Tools Page Meta Description"),
    ("cbse_calculator_meta_title", "CBSE Calculator Page Meta Title"),
    ("cbse_calculator_meta_desc", "CBSE Calculator Page Meta Description"),
    ("sslc_calculator_meta_title", "SSLC Calculator Page Meta Title"),
    ("sslc_calculator_meta_desc", "SSLC Calculator Page Meta Description"),
    ("cbse_calculator_12_meta_title", "CBSE 12 Calculator Page Meta Title"),
    ("cbse_calculator_12_meta_desc", "CBSE 12 Calculator Page Meta Description"),
    ("kerala_hsc_calculator_meta_title", "Kerala HSC Calculator Page Meta Title"),
    ("kerala_hsc_calculator_meta_desc", "Kerala HSC Calculator Page Meta Description"),
    ("tamilnadu_hsc_calculator_meta_title", "Tamilnadu HSC Calculator Page Meta Title"),
    ("tamilnadu_hsc_calculator_meta_desc", "Tamilnadu HSC Calculator Page Meta Description"),
    ("tamilnadu_sslc_calculator_meta_title", "Tamilnadu SSLC Calculator Page Meta Title"),
    ("tamilnadu_sslc_calculator_meta_desc", "Tamilnadu SSLC Calculator Page Meta Description"),
)


class Country(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    code = models.CharField(max_length=200)
    flag = models.CharField(max_length=400)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def get_listed_locations(self):
        return Location.objects.filter(country=self, is_active=True, show_in_page=True)

    def __str__(self):
        return self.name


class Slider(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="slider/")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"

    def __str__(self):
        return self.title


class Achievement(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="achievement/")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Achievement"
        verbose_name_plural = "Achievements"

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


class AcademicProgram(models.Model):
    program_type = models.CharField(max_length=200, choices=(("ACADEMIC", "ACADEMIC COURSE"), ("LANGUAGE", "LANGUAGE COURSE")), default="ACADEMIC")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    logo = models.ImageField(upload_to="program/", blank=True, null=True)
    image = models.ImageField(upload_to="program/")
    content = CKEditor5Field(blank=True, null=True, config_name="extends")
    lessons = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=200, blank=True, null=True)
    duration = models.CharField(max_length=200, blank=True, null=True)
    preview_video_id = models.CharField(max_length=11, blank=True, null=True)
    show_in_navigation = models.BooleanField(default=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    meta_title = models.CharField(max_length=200)
    meta_description = models.TextField()

    def get_features(self):
        return ProgramFeature.objects.filter(program=self)

    def get_benefits(self):
        return ProgramBenefit.objects.filter(program=self)

    def get_faqs(self):
        return ProgramFAQ.objects.filter(program=self)

    def get_ctas(self):
        return [{"title": cta.title, "image": cta.image.url, "xpath": cta.xpath} for cta in AcademicProgramCTA.objects.filter(program=self).order_by("id")]

    def get_absolute_url(self):
        return reverse("web:course_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class AcademicProgramCTA(models.Model):
    program = models.ForeignKey(AcademicProgram, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="AcademicProgramCTA/")
    xpath = models.CharField(help_text="XPath of the element after which the CTA should be shown", max_length=300)

    class Meta:
        verbose_name = "Academic Program CTA"
        verbose_name_plural = "Academic Program CTAs"

    def __str__(self):
        return self.title


class ProgramFeature(models.Model):
    program = models.ForeignKey(AcademicProgram, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Program Feature"
        verbose_name_plural = "Program Features"

    def __str__(self):
        return self.title


class ProgramBenefit(models.Model):
    program = models.ForeignKey(AcademicProgram, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "Program Benefit"
        verbose_name_plural = "Program Benefits"

    def __str__(self):
        return self.title


class ProgramFAQ(models.Model):
    program = models.ForeignKey(AcademicProgram, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    answer = models.TextField()

    class Meta:
        verbose_name = "Program FAQ"
        verbose_name_plural = "Program FAQs"

    def __str__(self):
        return self.question


class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "General FAQ"
        verbose_name_plural = "General FAQs"

    def __str__(self):
        return self.question


class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    date = models.DateField()
    summary = models.TextField()
    image = models.ImageField(upload_to="blog/")
    content = CKEditor5Field(blank=True, null=True, config_name="extends")
    meta_title = models.CharField(max_length=200)
    meta_description = models.TextField()
    sequence = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering = ("sequence", "-date")

    def get_absolute_url(self):
        return reverse("web:news_detail", kwargs={"slug": self.slug})

    def get_ctas(self):
        return [{"title": cta.title, "image": cta.image.url, "xpath": cta.xpath} for cta in NewsCTA.objects.filter(news=self).order_by("id")]

    def __str__(self):
        return self.title


class NewsCTA(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="news/")
    xpath = models.CharField(help_text="XPath of the element after which the CTA should be shown", max_length=300)

    class Meta:
        verbose_name = "News CTA"
        verbose_name_plural = "News CTAs"

    def __str__(self):
        return self.title


class MediaFeature(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="feature/")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Media Feature"
        verbose_name_plural = "Media Features"

    def __str__(self):
        return self.title


class BlogCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"

    def blog_count(self):
        return Blog.objects.filter(category=self).count()

    def get_absolute_url(self):
        return reverse("web:blog_category_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name


class BlogAuthor(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="author/")
    bio = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Blog Author"
        verbose_name_plural = "Blog Authors"

    def __str__(self):
        return self.name


class AuthorSocialMedia(models.Model):
    author = models.ForeignKey(BlogAuthor, on_delete=models.CASCADE)
    icon = models.CharField(max_length=200, choices=MEDIA_CHOICES)
    url = models.URLField()

    class Meta:
        verbose_name = "Author Social Media"
        verbose_name_plural = "Author Social Media"

    def __str__(self):
        return self.icon


class Blog(models.Model):
    TEMPLATE_CHOICES = (
        ("web/blog_detail_1.html", "Default"),
        ("web/blog_detail_2.html", "Elegant"),
        ("web/blog_detail_3.html", "Classic"),
    )
    template = models.CharField(max_length=200, default="web/blog_detail_1.html", choices=TEMPLATE_CHOICES)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    author = models.ForeignKey(BlogAuthor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    summary = models.TextField()
    image = models.ImageField(upload_to="blog/")
    meta_title = models.CharField(max_length=200)
    meta_description = models.TextField()
    sequence = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ["-date"]
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def get_word_count(self):
        word_count = len(strip_tags(self.title).split())
        content = BlogContent.objects.filter(blog=self).order_by("id")
        for item in content:
            word_count += len(strip_tags(item.content).split())
        return word_count

    def get_image_dimensions(self):
        if self.image:
            width, height = get_image_dimensions(self.image)
            return (width, height)
        return (0, 0)

    def get_absolute_url(self):
        return reverse("web:blog_detail", kwargs={"slug": self.slug})

    def author_social_medias(self):
        return AuthorSocialMedia.objects.filter(author=self.author)

    def get_contents(self):
        return BlogContent.objects.filter(blog=self).order_by("id")

    def get_faqs(self):
        return BlogFAQ.objects.filter(blog=self).order_by("id")

    def get_ctas(self):
        return [{"title": cta.title, "image": cta.image.url, "xpath": cta.xpath} for cta in BlogCTA.objects.filter(blog=self).order_by("id")]

    def __str__(self):
        return self.title


class BlogContent(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = CKEditor5Field(blank=True, null=True, config_name="extends")

    class Meta:
        ordering = ["id"]
        verbose_name = "Blog Content"
        verbose_name_plural = "Blog Contents"

    def __str__(self):
        return self.title


class BlogFAQ(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    answer = models.TextField()

    class Meta:
        verbose_name = "Blog FAQ"
        verbose_name_plural = "Blog FAQs"

    def __str__(self):
        return self.question


class BlogCTA(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blog/")
    xpath = models.CharField(help_text="XPath of the element after which the CTA should be shown", max_length=300)

    class Meta:
        verbose_name = "Blog CTA"
        verbose_name_plural = "Blog CTAs"

    def __str__(self):
        return self.title


class Location(models.Model):
    TEMPLATE_CHOICES = (
        ("web/location_1.html", "Default"),
        ("web/location_2.html", "Elegant"),
        ("web/location_3.html", "Classic"),
    )
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="locations")
    template = models.CharField(max_length=200, default="web/location_1.html", choices=TEMPLATE_CHOICES)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    banner_image = models.ImageField(upload_to="location/")
    page_title = models.CharField(max_length=200)
    meta_title = models.CharField(max_length=200)
    meta_description = models.TextField()
    content = CKEditor5Field(blank=True, null=True, config_name="extends")
    is_active = models.BooleanField(default=True)
    show_in_page = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    def get_absolute_url(self):
        return reverse("web:location_detail", kwargs={"slug": self.slug})

    def get_faqs(self):
        return LocationFAQ.objects.filter(location=self)

    def get_cities(self):
        return City.objects.filter(location=self, is_active=True, show_in_page=True)

    def get_ctas(self):
        return [{"title": cta.title, "image": cta.image.url, "xpath": cta.xpath} for cta in LocationCTA.objects.filter(location=self).order_by("id")]

    def get_title(self):
        return f"{self.title}"

    def __str__(self):
        return self.title


class LocationFAQ(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    answer = models.TextField()

    class Meta:
        verbose_name = "Location FAQ"
        verbose_name_plural = "Location FAQs"

    def __str__(self):
        return self.question


class LocationCTA(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="locations/")
    xpath = models.CharField(help_text="XPath of the element after which the CTA should be shown", max_length=300)

    class Meta:
        verbose_name = "Location CTA"
        verbose_name_plural = "Location CTAs"

    def __str__(self):
        return self.title


class Subject(models.Model):
    subject = models.CharField(max_length=200)
    feature_heading = models.CharField(max_length=200, default="Key Features of Our Tailored Learning Experience")
    icon = models.ImageField(upload_to="subject/")
    slug = models.SlugField(max_length=200, unique=True)
    banner_image = models.ImageField(upload_to="subject/")
    page_title = models.CharField(max_length=200)
    meta_title = models.CharField(max_length=200)
    page_description = models.TextField()
    meta_description = models.TextField()
    content = CKEditor5Field(blank=True, null=True, config_name="extends")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def get_absolute_url(self):
        return reverse("web:subject_detail", kwargs={"slug": self.slug})

    def get_title(self):
        return f"{self.subject}"

    def get_features(self):
        return SubjectFeature.objects.filter(subject=self)

    def get_faqs(self):
        return SubjectFAQ.objects.filter(subject=self)

    def __str__(self):
        return self.subject


class SubjectFeature(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "Subject Detail"
        verbose_name_plural = "Subject Details"

    def __str__(self):
        return self.title


class SubjectFAQ(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    answer = models.TextField()

    class Meta:
        verbose_name = "Subject FAQ"
        verbose_name_plural = "Subject FAQs"

    def __str__(self):
        return self.question


class Board(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="board/")
    page_title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = CKEditor5Field(blank=True, null=True, config_name="extends")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Board"
        verbose_name_plural = "Boards"

    def get_absolute_url(self):
        return reverse("web:board_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name


class ResourceCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Resource Category"
        verbose_name_plural = "Resource Categories"

    def __str__(self):
        return self.name


class Resource(models.Model):
    category = models.ForeignKey(ResourceCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="resource/")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Resource"
        verbose_name_plural = "Resources"

    def __str__(self):
        return self.title


class Staff(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    bio = models.TextField()
    image = models.ImageField(upload_to="staff/")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staffs"

    def __str__(self):
        return self.name


class Enquiry(models.Model):
    name = models.CharField(max_length=200)
    country = CountryField()
    phone_number = models.CharField("Phone Number", max_length=25)
    whatsapp_number = models.CharField("WhatsApp Number", max_length=25)
    email = models.EmailField(blank=True, null=True)
    purpose = models.ForeignKey("Purpose", on_delete=models.CASCADE, blank=True, null=True)
    message = models.TextField("Drop your message here", blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # Fields for UTM parameters
    utm_source = models.CharField(max_length=255, blank=True, null=True)
    utm_medium = models.CharField(max_length=255, blank=True, null=True)
    utm_campaign = models.CharField(max_length=255, blank=True, null=True)
    utm_content = models.CharField(max_length=255, blank=True, null=True)
    utm_term = models.CharField(max_length=255, blank=True, null=True)

    token = models.UUIDField(default=uuid.uuid4, editable=False)
    otp_number = models.CharField(max_length=6, blank=True, null=True)
    attempt = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)
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


class ContactData(models.Model):
    name = models.CharField(max_length=200)
    country = CountryField()
    phone_number = models.CharField("Phone Number", max_length=25)
    whatsapp_number = models.CharField("WhatsApp Number", max_length=25)
    email = models.EmailField(blank=True, null=True)
    purpose = models.ForeignKey("Purpose", on_delete=models.CASCADE, blank=True, null=True)
    message = models.TextField("Drop your message here", blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # Fields for UTM parameters
    utm_source = models.CharField(max_length=255, blank=True, null=True)
    utm_medium = models.CharField(max_length=255, blank=True, null=True)
    utm_campaign = models.CharField(max_length=255, blank=True, null=True)
    utm_content = models.CharField(max_length=255, blank=True, null=True)
    utm_term = models.CharField(max_length=255, blank=True, null=True)

    token = models.UUIDField(default=uuid.uuid4, editable=False)
    otp_number = models.CharField(max_length=6, blank=True, null=True)
    attempt = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)
    is_sent2crm = models.BooleanField(default=False)

    lsq_status_code = models.IntegerField(blank=True, null=True)
    lsq_status = models.CharField(max_length=200, blank=True, null=True)
    lsq_exception_type = models.TextField(blank=True, null=True)
    lsq_exception_message = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Contact Data"
        verbose_name_plural = "Contact Datas"

    def __str__(self):
        return self.name


class GeneralFeature(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "General Feature"
        verbose_name_plural = "General Features"

    def __str__(self):
        return self.title


class DemoRequest(models.Model):
    raised_by = models.CharField(
        "I'am a",
        max_length=200,
        choices=(
            ("STUDENT", "Student"),
            ("PARENT", "Parent"),
            ("GUARDIAN", "Guardian"),
        ),
    )
    student_name = models.CharField(max_length=200)
    email = models.EmailField()
    country = CountryField()
    phone_number = models.CharField("Phone Number", max_length=20)
    whatsapp_number = models.CharField("WhatsApp Number", max_length=20)
    standard = models.CharField("Class", max_length=200, choices=CLASS_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=200,
        choices=(
            ("PENDING", "Pending"),
            ("APPROVED", "Approved"),
            ("REJECTED", "Rejected"),
        ),
        default="PENDING",
    )
    # Fields for UTM parameters
    utm_source = models.CharField(max_length=255, blank=True, null=True)
    utm_medium = models.CharField(max_length=255, blank=True, null=True)
    utm_campaign = models.CharField(max_length=255, blank=True, null=True)
    utm_content = models.CharField(max_length=255, blank=True, null=True)
    utm_term = models.CharField(max_length=255, blank=True, null=True)

    token = models.UUIDField(default=uuid.uuid4, editable=False)
    otp_number = models.CharField(max_length=6, blank=True, null=True)
    attempt = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)
    is_sent2crm = models.BooleanField(default=False)

    lsq_status_code = models.IntegerField(blank=True, null=True)
    lsq_status = models.CharField(max_length=200, blank=True, null=True)
    lsq_exception_type = models.TextField(blank=True, null=True)
    lsq_exception_message = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Demo Request"
        verbose_name_plural = "Demo Requests"

    def __str__(self):
        return self.student_name


class SocialMedia(models.Model):
    icon = models.CharField(max_length=200, choices=MEDIA_CHOICES)
    url = models.URLField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Social Media"
        verbose_name_plural = "Social Media"

    def __str__(self):
        return self.icon


class NonAcademicProgram(models.Model):
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to="program/")
    program_type = models.CharField(max_length=200, choices=PROGRAM_TYPE_CHOICES, default="ACADEMIC")
    course_fee = models.DecimalField(max_digits=10, decimal_places=0, default=0)

    duration = models.CharField(max_length=200, blank=True, null=True)
    age_groups = MultiSelectField(max_length=200, choices=AGEGROUP_CHOICES, blank=True, null=True)
    lessons = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=200, blank=True, null=True)
    is_certificate_included = models.BooleanField(default=True, blank=True, null=True)
    preview_video_id = models.CharField(max_length=11, blank=True, null=True)

    content = CKEditor5Field("About", blank=True, null=True, config_name="extends")
    learning_overview = CKEditor5Field("Learning Overview", blank=True, null=True, config_name="extends")
    show_learning_overview = models.BooleanField("Show Learning Overview", default=True)

    meta_title = models.CharField(max_length=200)
    meta_description = models.TextField()

    def available_times(self):
        return NonAcademicProgramTime.objects.filter(program=self)

    def get_absolute_url(self):
        return reverse("web:nac_course_detail", kwargs={"slug": self.slug})

    def get_form_url(self):
        return reverse("web:course_form", kwargs={"slug": self.slug})

    def get_age_groups(self):
        return " ".join(self.age_groups)

    def get_ctas(self):
        pass

    def __str__(self):
        return self.title


class NonAcademicProgramCTA(models.Model):
    program = models.ForeignKey(NonAcademicProgram, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="NonAcademicProgramCTA/")
    xpath = models.CharField(help_text="XPath of the element after which the CTA should be shown", max_length=300)

    class Meta:
        verbose_name = "Non Academic Program CTA"
        verbose_name_plural = "Non Academic Program CTAs"

    def __str__(self):
        return self.title


class NonAcademicProgramTime(models.Model):
    program = models.ForeignKey(NonAcademicProgram, on_delete=models.CASCADE)
    day = models.CharField(max_length=200)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        verbose_name = "Program Time"
        verbose_name_plural = "Program Times"

    def __str__(self):
        return f"{self.program.title} - {self.day}"


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    student_name = models.CharField(max_length=200)
    email = models.EmailField()
    country = CountryField()
    state = models.CharField("State/Province", max_length=200)
    phone_number = models.CharField("Phone Number", max_length=20)
    whatsapp_number = models.CharField("WhatsApp Number", max_length=20)
    standard = models.CharField("Class", max_length=200, choices=CLASS_CHOICES)
    referred_by = models.CharField(max_length=200, blank=True, null=True)

    course = models.ForeignKey(NonAcademicProgram, on_delete=models.CASCADE, blank=True, null=True)
    coupon = models.ForeignKey("Coupon", on_delete=models.SET_NULL, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=200, blank=True, null=True)
    razorpay_order_id = models.CharField(max_length=200, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=200, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=200, blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(blank=True, null=True)

    def payable(self):
        return self.amount - self.discount_amount

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    def __str__(self):
        return self.student_name


class About(models.Model):
    address = models.TextField()
    phone = models.CharField("Phone Number", max_length=20)
    whatsapp = models.CharField("WhatsApp Number", max_length=20)
    email = models.EmailField()

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"

    def __str__(self):
        return "Change About"


class City(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="cities")
    name = models.CharField(max_length=200)
    page_title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    meta_title = models.CharField(max_length=200)
    meta_description = models.TextField()
    content = CKEditor5Field(blank=True, null=True, config_name="extends")
    is_active = models.BooleanField(default=True)
    show_in_page = models.BooleanField("Show in Location Page", default=True)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def get_absolute_url(self):
        return reverse("web:city_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name


class Coupon(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    name = models.CharField("Coupon Name", max_length=200)
    code = models.CharField("Coupon Code", max_length=200, unique=True)
    applicable_courses = models.ManyToManyField(NonAcademicProgram, blank=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Enter discount in percentage")
    is_active = models.BooleanField("Is Active", default=True)

    def used_count(self):
        return Payment.objects.filter(coupon=self.code).count()

    def save(self, *args, **kwargs):
        self.code = self.code.upper()
        super().save(*args, **kwargs)

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


class Purpose(models.Model):
    name = models.CharField(max_length=200)
    enable_redirect = models.BooleanField(default=False)
    redirect_url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Purpose"
        verbose_name_plural = "Purposes"

    def __str__(self):
        return self.name
