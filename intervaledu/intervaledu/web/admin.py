from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from .models import (
    FAQ,
    About,
    Purpose,
    AcademicProgram,
    AcademicProgramCTA,
    Achievement,
    AuthorSocialMedia,
    Blog,
    BlogCTA,
    BlogAuthor,
    BlogCategory,
    BlogContent,
    BlogFAQ,
    Board,
    City,
    Configuration,
    ContactData,
    Country,
    Coupon,
    DemoRequest,
    Enquiry,
    GeneralFeature,
    Location,
    LocationFAQ,
    LocationCTA,
    MediaFeature,
    News,
    NewsCTA,
    NonAcademicProgram,
    NonAcademicProgramCTA,
    NonAcademicProgramTime,
    Payment,
    ProgramBenefit,
    ProgramFAQ,
    ProgramFeature,
    Resource,
    ResourceCategory,
    Slider,
    SocialMedia,
    Staff,
    Subject,
    SubjectFAQ,
    SubjectFeature,
    Testimonial,
)


class ProgramFeatureInline(admin.TabularInline):
    model = ProgramFeature
    extra = 1


class ProgramBenefitInline(admin.StackedInline):
    model = ProgramBenefit
    extra = 1


class ProgramFAQInline(admin.StackedInline):
    model = ProgramFAQ
    extra = 1


class SubjectFeatureInline(admin.StackedInline):
    model = SubjectFeature
    extra = 1


class SubjectFAQInline(admin.StackedInline):
    model = SubjectFAQ
    extra = 1


class BlogContentInline(admin.StackedInline):
    model = BlogContent
    extra = 0


class BlogCTAInline(admin.StackedInline):
    model = BlogCTA
    extra = 1


class AuthorSocialMediaInline(admin.TabularInline):
    model = AuthorSocialMedia
    extra = 1


class LocationFAQInline(admin.StackedInline):
    model = LocationFAQ
    extra = 1


class BlogFAQInline(admin.StackedInline):
    model = BlogFAQ
    extra = 1


class NonAcademicProgramTimeInline(admin.TabularInline):
    model = NonAcademicProgramTime
    extra = 1


@admin.register(About)
class AboutAdmin(ImportExportActionModelAdmin):
    list_display = ("__str__",)
    search_fields = ("__str__",)


@admin.register(Country)
class CountryAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "slug", "is_active")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("is_active",)


@admin.register(Slider)
class SliderAdmin(ImportExportActionModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(Achievement)
class AchievementAdmin(ImportExportActionModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(Testimonial)
class TestimonialAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "designation")
    search_fields = ("name", "designation")


class AcademicProgramCTAInline(admin.StackedInline):
    model = AcademicProgramCTA
    extra = 0


@admin.register(AcademicProgram)
class AcademicProgramAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "duration", "language")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    inlines = (ProgramFeatureInline, ProgramBenefitInline, ProgramFAQInline, AcademicProgramCTAInline)


@admin.register(FAQ)
class FAQAdmin(ImportExportActionModelAdmin):
    list_display = ("question",)
    search_fields = ("question",)


class NewsCTAInline(admin.StackedInline):
    model = NewsCTA
    extra = 0


@admin.register(News)
class NewsAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "date", "sequence")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    inlines = (NewsCTAInline,)


@admin.register(MediaFeature)
class MediaFeatureAdmin(ImportExportActionModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(BlogCategory)
class BlogCategoryAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "slug", "blog_count")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(BlogAuthor)
class BlogAuthorAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "bio")
    search_fields = ("name",)
    inlines = (AuthorSocialMediaInline,)


@admin.register(Blog)
class BlogAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "category", "author", "date", "sequence")
    search_fields = ("title", "slug")
    list_filter = ("category", "author")
    prepopulated_fields = {"slug": ("title",)}
    inlines = (BlogContentInline, BlogFAQInline, BlogCTAInline)


class LocationCTAInline(admin.StackedInline):
    model = LocationCTA
    extra = 0


@admin.register(Location)
class LocationAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "template", "country", "is_active")
    list_filter = ("country", "is_active")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    inlines = (LocationFAQInline, LocationCTAInline)
    autocomplete_fields = ("country",)


@admin.register(Subject)
class SubjectAdmin(ImportExportActionModelAdmin):
    list_display = ("subject",)
    search_fields = ("subject",)
    prepopulated_fields = {"slug": ("subject",)}
    inlines = (SubjectFeatureInline, SubjectFAQInline)


@admin.register(Enquiry)
class EnquiryAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "country", "phone_number", "whatsapp_number", "timestamp", "purpose", "lsq_status_code")
    search_fields = ("name", "country", "phone_number", "whatsapp_number")
    list_filter = ("purpose", "lsq_status_code", "lsq_status", "lsq_exception_type", "lsq_exception_message")


@admin.register(ContactData)
class ContactDataAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "country", "phone_number", "whatsapp_number", "timestamp", "purpose")
    search_fields = ("name", "country", "phone_number", "whatsapp_number")
    list_filter = ("purpose", "timestamp", "country")


@admin.register(Board)
class BoardAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "logo", "is_active")
    search_fields = ("name",)


@admin.register(ResourceCategory)
class ResourceCategoryAdmin(ImportExportActionModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Resource)
class ResourceAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "file")
    list_filter = ("category",)
    search_fields = ("title",)


@admin.register(Staff)
class StaffAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "designation")
    search_fields = ("name", "designation")


@admin.register(GeneralFeature)
class GeneralFeatureAdmin(ImportExportActionModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(DemoRequest)
class DemoRequestAdmin(ImportExportActionModelAdmin):
    list_display = ("raised_by", "student_name", "email", "phone_number", "status", "timestamp")
    search_fields = ("student_name", "email", "phone_number")
    list_filter = ("raised_by", "status", "timestamp")


@admin.register(SocialMedia)
class SocialMediaAdmin(ImportExportActionModelAdmin):
    list_display = ("icon", "url")


@admin.register(Payment)
class PaymentAdmin(ImportExportActionModelAdmin):
    list_display = ("student_name", "session_id", "course", "coupon", "amount", "payable", "is_paid", "paid_at", "created_at")
    search_fields = ("student_name", "session_id", "created_at")
    list_display_links = ("student_name", "session_id")
    list_filter = ("is_paid", "course", "coupon", "created_at", "paid_at")


class NonAcademicProgramCTAInline(admin.StackedInline):
    model = NonAcademicProgramCTA
    extra = 0


@admin.register(NonAcademicProgram)
class NonAcademicProgramAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "duration", "program_type", "language", "is_certificate_included")
    list_filter = ("program_type", "language", "is_certificate_included")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    inlines = (NonAcademicProgramTimeInline, NonAcademicProgramCTAInline)


@admin.register(City)
class CityAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "slug", "is_active", "show_in_page")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("page_title",)}
    list_filter = ("is_active", "show_in_page")
    autocomplete_fields = ("location",)


@admin.register(Coupon)
class CouponAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "code", "discount", "is_active")
    search_fields = ("code",)
    list_filter = ("is_active",)
    autocomplete_fields = ("applicable_courses",)


@admin.register(BlogContent)
class BlogContentAdmin(ImportExportActionModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(Configuration)
class ConfigurationAdmin(ImportExportActionModelAdmin):
    list_display = ("key", "summary")
    search_fields = ("key",)

    def summary(self, obj):
        return (obj.value[:100] + "...") if len(obj.value) > 100 else obj.value


@admin.register(Purpose)
class PurposeAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "enable_redirect", "redirect_url")
    search_fields = ("name",)
