import datetime

from django import template

register = template.Library()


@register.filter
def format_duration(duration):
    if isinstance(duration, datetime.timedelta):
        total_seconds = duration.total_seconds()
        milliseconds = int((total_seconds * 1000) % 1000)
        formatted_duration = "{:02}:{:02}:{:02}.{:02}".format(int(total_seconds // 3600), int((total_seconds % 3600) // 60), int(total_seconds % 60), milliseconds // 10)
        return formatted_duration
    return duration  # Return the original duration if it's not a timedelta
