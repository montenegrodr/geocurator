from enum import Enum


class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude


class Customer:
    def __init__(self, id, name, latitude, longitude):
        self.id = id
        self.name = name
        self.location = Location(latitude,
                                 longitude)

    def location(self):
        return self.location

    @staticmethod
    def from_str(str, decoder):
        raise NotImplementedError()

    def to_str(self, encoder):
        raise NotImplementedError()


class Parsers(Enum):
    JSON = 1


class Parser:
    @staticmethod
    def factory(parser=Parsers.JSON):
        if parser == Parsers.JSON:
            return JSONParser()
        else:
            raise NotImplementedError(
                f'Parser \"{parser}\" not found')

    def encode(self, obj):
        raise NotImplementedError()

    def decode(self, obj):
        raise NotImplementedError()


class JSONParser(Parser):
    def encode(self, obj):
        raise NotImplementedError()

    def decode(self, obj):
        raise NotImplementedError()
