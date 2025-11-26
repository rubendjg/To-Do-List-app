from .user_views import *
from .task_views import *
from .general_views import *
from django.http import JsonResponse
from django.utils.timezone import now
import os


def health(request):
    """
    Health check endpoint
    Returns basic status of the app.
    """
    return JsonResponse({
        "status": "ok",
        "time": now(),
        "environment": os.getenv("DJANGO_SETTINGS_MODULE", "unknown"),
    })