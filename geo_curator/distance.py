from geopy.distance import great_circle


class DistanceCalculator:
    def distance(self, a, b):
        raise NotImplementedError()


class GreatCircle(DistanceCalculator):
    def distance(self, a, b):
        return great_circle(
            (a.latitude, a.longitude),
            (b.latitude, b.longitude)
        ).kilometers
