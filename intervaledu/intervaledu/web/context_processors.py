from web.models import About, AcademicProgram, Location, Slider, SocialMedia, Subject, Purpose
import json
from django.core.cache import cache
from .forms import DemoRequestForm, EnquiryPopupForm

meta_title = "Best Online Tuition Classes & Academic & Non-Academic Courses | Interval Learning"
meta_description = "Interval Learning is the best online platform that provides personalized courses. We offer both academic and non-academic courses that help your child's growth. Our programs are completely personalized and conducted one-on-one."


def main_context(request):
    # Cache expensive queries that don't change often
    cache_key_base = "main_context_"

    # Get cached data or fetch from database
    ac_programs_cache_key = cache_key_base + "ac_programs"
    ac_programs = cache.get(ac_programs_cache_key)
    if ac_programs is None:
        ac_programs = list(AcademicProgram.objects.filter(is_active=True).only("id", "title", "slug", "show_in_navigation", "program_type"))
        cache.set(ac_programs_cache_key, ac_programs, 600)  # Cache for 10 minutes

    locations_cache_key = cache_key_base + "locations"
    locations = cache.get(locations_cache_key)
    if locations is None:
        locations = list(Location.objects.filter(is_active=True).only("id", "title", "slug"))
        cache.set(locations_cache_key, locations, 600)

    subjects_cache_key = cache_key_base + "subjects"
    subjects = cache.get(subjects_cache_key)
    if subjects is None:
        subjects = list(Subject.objects.filter(is_active=True).only("id", "subject", "slug"))
        cache.set(subjects_cache_key, subjects, 600)

    social_medias_cache_key = cache_key_base + "social_medias"
    social_medias = cache.get(social_medias_cache_key)
    if social_medias is None:
        social_medias = list(SocialMedia.objects.filter(is_active=True).only("id", "icon", "url"))
        cache.set(social_medias_cache_key, social_medias, 600)

    about_cache_key = cache_key_base + "about"
    about = cache.get(about_cache_key)
    if about is None:
        about = About.objects.first()
        cache.set(about_cache_key, about, 600)

    first_slider_cache_key = cache_key_base + "first_slider"
    first_slider = cache.get(first_slider_cache_key)
    if first_slider is None:
        first_slider = Slider.objects.filter(is_active=True).only("title", "image").first()
        cache.set(first_slider_cache_key, first_slider, 600)

    purposes_json_cache_key = cache_key_base + "purposes_json"
    purposes_json = cache.get(purposes_json_cache_key)
    if purposes_json is None:
        purposes_json = json.dumps(list(Purpose.objects.all().only("id", "name", "enable_redirect", "redirect_url").values("id", "name", "enable_redirect", "redirect_url")))
        cache.set(purposes_json_cache_key, purposes_json, 600)

    # Optimize: filter once and reuse
    nav_programs = [p for p in ac_programs if p.show_in_navigation]
    nav_locations = nav_programs  # This seems to be a duplicate, keeping for compatibility

    domain = "https://" + request.get_host()
    og_url = domain + request.path

    # Forms are lightweight, instantiate them (needed for modals in base.html)
    enquiry_form = EnquiryPopupForm(request.POST or None)
    demo_request_form = DemoRequestForm(request.POST or None)

    utm_params = ["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term"]
    for param in utm_params:
        value = request.GET.get(param)
        if value:
            request.session[param] = value

    return {
        "locations": locations,
        "subjects": subjects,
        "enquiry_form": enquiry_form,
        "demo_request_form": demo_request_form,
        "nav_locations": nav_locations,
        "nav_programs": nav_programs,
        "ac_programs": ac_programs,
        "social_medias": social_medias,
        "domain": domain,
        "about": about,
        "first_slider": first_slider,
        "meta_title": meta_title,
        "meta_description": meta_description,
        "og_url": og_url,
        "purposes_json": purposes_json,
    }
