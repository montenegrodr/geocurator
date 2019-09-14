import unittest
import numpy as np

from geo_curator.distance import GreatCircle
from geo_curator.parser import Location


class TestDistance(unittest.TestCase):
    def setUp(self):
        self.office = Location(53.339428, -6.257664)
        self.torre = Location(8.0438077, -34.9134957)
        self.temple_bar = Location(53.3454325, -6.2668687)

    def test_short_distance(self):
        np.testing.assert_almost_equal(
            actual=GreatCircle().distance(
                self.office, self.temple_bar
            ),
            desired=0.9050916
        )

    def test_long_distance(self):
        np.testing.assert_almost_equal(
            actual=GreatCircle().distance(
                self.office, self.torre
            ),
            desired=5656.8585267
        )

    def test_great_circle_all_zero(self):
        assert GreatCircle().distance(
            Location(latitude=0, longitude=0),
            Location(latitude=0, longitude=0)
        ) == 0, "All zero distance should be 0"
