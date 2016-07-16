from datetime import timedelta
from functools import wraps

import geojson

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from surfers import api
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
    collection = geojson.FeatureCollection([
        geojson.Feature(
            geometry=geojson.Point(i.point.coords),
            properties={
                'user': i.user.get_full_name(),
                'user_url': api.user.get_resource_uri(i.user),
                'updated_at': i.updated_at.isoformat(),
            }
        )
        for i in points
    ])
    return HttpResponse(geojson.dumps(collection), content_type='application/json')
