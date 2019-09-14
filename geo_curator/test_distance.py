import unittest

from geo_curator.distance import GreatCircle
from geo_curator.parser import Location

PRECISION = 1


class TestDistance(unittest.TestCase):
    def setUp(self):
        self.office = Location(53.339428, -6.257664)
        self.torre = Location(8.0438077, -34.9134957)
        self.temple_bar = Location(53.3454325, -6.2668687)

    def test_short_distance(self):
        self.assertAlmostEqual(
            first=GreatCircle().distance(
                self.office, self.temple_bar
            ),
            second=0.9050916,
            places=PRECISION
        )

    def test_long_distance(self):
        self.assertAlmostEqual(
            first=GreatCircle().distance(
                self.office, self.torre
            ),
            second=5656.8585267,
            places=PRECISION
        )

    def test_great_circle_all_zero(self):
        assert GreatCircle().distance(
            Location(latitude=0, longitude=0),
            Location(latitude=0, longitude=0)
        ) == 0, "All zero distance should be 0"
