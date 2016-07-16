from datetime import timedelta
from functools import wraps

from django.conf import settings
from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from surfers.models import LatestPoint


def login_required(f):
    @wraps(f)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated():
            return f(request, *args, **kwargs)
        else:
            return HttpResponse('Log in first, please!', status=401)
    return wrapper


@login_required
def sunmap(request):
    return render(request, 'sunmap.html', {
        'mapbox_token': settings.MAPBOX_TOKEN
    })


@login_required
def latest(request):
    points = LatestPoint.objects.filter(
        updated_at__gt=timezone.now() - timedelta(days=14),
    ).order_by('-updated_at')[:100]
    return HttpResponse(serialize(
        'geojson', points, geometry_field='point',
        fields=('user.username', 'updated_at')
    ), content_type='application/json')
