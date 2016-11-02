'''
Created on Jul 29, 2015

@author: apechenk
'''

import json
from django.http.response import HttpResponse

from .models import Artist

import logging
L = logging.getLogger(__name__)


def artist_search(request):
    params = request.GET.dict()
    rows = Artist.objects.best_age_match(params)
    return HttpResponse(json.dumps([(r.uuid, r.age) for r in rows]), content_type='application/json')
