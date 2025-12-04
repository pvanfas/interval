

meta_title = "Best Online Tuition Classes & Academic & Non-Academic Courses | Interval Learning"
meta_description = "Interval Learning is the best online platform that provides personalized courses. We offer both academic and non-academic courses that help your child's growth. Our programs are completely personalized and conducted one-on-one."


def main_context(request):
    domain = "https://" + request.get_host()
    og_url = domain + request.path

    utm_params = ["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term"]
    for param in utm_params:
        value = request.GET.get(param)
        if value:
            request.session[param] = value

    return {
        "domain": domain,
        "meta_title": meta_title,
        "meta_description": meta_description,
        "og_url": og_url,
    }
