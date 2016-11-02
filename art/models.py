'''
Created on Jul 29, 2015

@author: apechenk
'''

from django.db import models
from django.db.models import F, Func

import logging
L = logging.getLogger(__name__)


class ArtistManager(models.Manager):
    def best_age_match(self, params):
        rows = self.filter(**params)
        if 'age__lte' in params and 'age__gte' in params:
            mean_age = (int(params['age__lte']) + int(params['age__gte']))/2
            L.debug('mean age=%s', mean_age)
            rows = rows.order_by(Func(F('age') - mean_age, function='ABS').asc())
        return rows


class Artist(models.Model):
    age = models.PositiveSmallIntegerField()
    uuid = models.CharField(max_length=36)

    objects = ArtistManager()
