import json
import logging
from enum import Enum

logger = logging.getLogger('geo_curator')


class Location:
    def __init__(self, latitude, longitude):
        self.latitude = float(latitude)
        self.longitude = float(longitude)


class Customer:
    def __init__(self, id, name, latitude, longitude):
        self.id = int(id)
        self.name = name
        self.location = Location(latitude,
                                 longitude)

    def __gt__(self, other):
        return self.id >= other.id

    def __lt__(self, other):
        return self.id < other.id

    def __repr__(self):
        return f'Customer({self.name}, ' \
               f'{self.id})'

    @staticmethod
    def from_str(str, decoder):
        return decoder.decode(str)

    def to_str(self, encoder):
        return encoder.encode(self)


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


class JSONParserDecodeException(Exception):
    pass


class JSONParser(Parser):
    def encode(self, obj):
        return json.dumps({
            'name': obj.name,
            'user_id': obj.id,
            'latitude': obj.location.latitude,
            'longitude': obj.location.longitude
        })

    def decode(self, obj):
        try:
            j = json.loads(obj)
            return Customer(
                id=j['user_id'],
                name=j['name'],
                latitude=j['latitude'],
                longitude=j['longitude']
            )
        except KeyError as e:
            logger.exception(e)
            raise JSONParserDecodeException(f'Error while decoding json: {e}')
