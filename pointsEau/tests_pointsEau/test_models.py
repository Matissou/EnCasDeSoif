from django.test import TestCase
from django.contrib.auth.models import User
from pointsEau.models import PointEau

# Create your tests here.


class SimpleTestPointEau(TestCase):

    # Create a user and add 3 points eau for him
    def setUp(self):
        user = User.objects.create_user(username='temporary', email='temporary@gmail.com', password='temporary')
        PointEau.objects.create(nom="Premier point", lat=43.099999999, long=34.0000000009, desc="A test point eau", owner=user)
        PointEau.objects.create(nom="point deux", lat=12.099999999, long=54.099999999, desc="A test point eau", owner=user)
        PointEau.objects.create(nom="point trois", lat=34.0099999999, long=22.0099999999, desc="A test point eau", owner=user)

    def testGetPointEauBasique(self):
        peau = PointEau.objects.all()
        self.assertEqual(len(peau), 3, "Number of point eau should be equal to 3 but actual number is {0}".format(len(peau)))

    def testGetUserPointEau(self):
        user = User.objects.get(username='temporary')
        ownerPeau = user.pointseau.all()
        self.assertEqual(len(ownerPeau), 3, "Number of point eau owned by user should be equal to 3 but actual number is {0}".format(len(ownerPeau)))

    def testDeleteUserPointEauDeleted(self):
        user = User.objects.get(username='temporary')
        user.delete()
        pEau = PointEau.objects.all()
        self.assertEqual(len(pEau), 0, "Number of point eau should be equal to 0 but actual number is {0}".format(len(pEau)))
