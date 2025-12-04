"""
Performance optimization utilities
Add caching decorators to your views for better performance
"""

from functools import wraps
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

# Cache times in seconds
CACHE_1_MINUTE = 60
CACHE_5_MINUTES = 300
CACHE_15_MINUTES = 900
CACHE_1_HOUR = 3600
CACHE_1_DAY = 86400
CACHE_1_WEEK = 604800


def cache_view(timeout=CACHE_5_MINUTES):
    """
    Simple cache decorator for views
    Usage: @cache_view(CACHE_15_MINUTES)
    """
    return cache_page(timeout)


def cache_for_anonymous(timeout=CACHE_5_MINUTES):
    """
    Cache decorator that only caches for anonymous users
    Authenticated users always get fresh content
    """

    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                # Don't cache for authenticated users
                return view_func(request, *args, **kwargs)
            else:
                # Cache for anonymous users
                return cache_page(timeout)(view_func)(request, *args, **kwargs)

        return wrapper

    return decorator


def conditional_cache(timeout=CACHE_5_MINUTES, key_prefix=""):
    """
    Conditional caching based on request parameters
    """

    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            # Build cache key from view name and parameters
            cache_key = f"{key_prefix}:{view_func.__name__}:{request.path}"

            # Try to get from cache
            cached_response = cache.get(cache_key)
            if cached_response is not None:
                return cached_response

            # Generate response
            response = view_func(request, *args, **kwargs)

            # Cache the response
            cache.set(cache_key, response, timeout)
            return response

        return wrapper

    return decorator


# Class-based view decorators
class CachedViewMixin:
    """
    Mixin for class-based views to add caching
    Usage: class MyView(CachedViewMixin, ListView):
               cache_timeout = CACHE_15_MINUTES
    """

    cache_timeout = CACHE_5_MINUTES

    @method_decorator(cache_page(cache_timeout))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# Usage Examples:
"""
# Function-based view
from web.performance_utils import cache_view, CACHE_15_MINUTES

@cache_view(CACHE_15_MINUTES)
def index(request):
    # Your view code
    pass

# Cache only for anonymous users
from web.performance_utils import cache_for_anonymous

@cache_for_anonymous(CACHE_5_MINUTES)
def blog_list(request):
    # Your view code
    pass

# Class-based view
from web.performance_utils import CachedViewMixin

class BlogListView(CachedViewMixin, ListView):
    cache_timeout = 300  # 5 minutes
    model = Blog
    template_name = 'blog_list.html'
"""
