from geopy.distance import great_circle


class DistanceCalculator:
    """
    Abstract class for distance calculation
    """
    def distance(self, a, b):
        raise NotImplementedError()


class GreatCircle(DistanceCalculator):
    def distance(self, a, b):
        """
        Calculate great circle distance between `a` and `b`
        Parameters
        ----------
        a : geo_curator.parser.Location
            first location
        b : geo_curator.parser.Location
            second location

        Returns
        -------
        float
            distance between `a` and `b` in kilometers
        """
        return great_circle(
            (a.latitude, a.longitude),
            (b.latitude, b.longitude)
        ).kilometers
