'''
Created on Jul 30, 2015

@author: apechenk
'''

from django.core.management import call_command
from django.test import TestCase
from .models import Artist


class ArtistSearchTestCase(TestCase):
    def setUp(self):
        call_command('loaddata', 'artist', verbosity=1)

    def test_mean_comes_first(self):
        for min_age in range(0, 90):
            for max_age in range(min_age, 100):
                mean_age = (min_age + max_age)/2
                rows = Artist.objects.best_age_match(dict(age__gte=min_age, age__lte=max_age))
                mean_dev = 0
                for row in rows:
                    new_mean_dev = abs(row.age - mean_age)
                    self.assertGreaterEqual(new_mean_dev, mean_dev, 'Deviation from mean age decreases: %s < %s, row=%s' % (new_mean_dev, mean_dev, row))
                    mean_dev = new_mean_dev