import json
from enum import Enum

LAT_MIN = -90
LAT_MAX = 90
LONG_MIN = -180
LONG_MAX = 180


class IllegalLocationException(Exception):
    pass


class Location:
    """
    Location point based on Latitude and Longitude coordinates
    """
    def __init__(self, latitude, longitude):
        """
        Parameters
        ----------
        latitude : float
            latitude coordinate
        longitude : float
            longitude coordinate
        """
        self.latitude = float(latitude)
        self.longitude = float(longitude)

        if self.latitude < LAT_MIN or self.latitude > LAT_MAX:
            raise IllegalLocationException(
                f'Latitude should be in the range ({LAT_MIN}, {LAT_MAX}).'
                f'Found {self.latitude} instead'
            )
        if self.longitude < LONG_MIN or self.longitude > LONG_MAX:
            raise IllegalLocationException(
                f'Longitude should be in the range ({LONG_MIN}, {LONG_MAX}).'
                f'Found {self.longitude} instead'
            )


class Customer:
    """
    Customer class representation
    """
    def __init__(self, id, name, latitude, longitude):
        """
        Parameters
        ----------
        id : str/int
            customer's unique identifier
        name : str
            customer's name
        latitude : float
            customer's location latitude coordinate
        longitude : float
            customer's location coordinate
        """
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
    """
    Abstract class for customer's object encoding decoding
    """
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
        """
        Encode customer object into a json string

        Parameters
        ----------
        obj : Customer
            customer object

        Returns
        -------
        str
           customer object json encoded into a string
        """
        return json.dumps({
            'name': obj.name,
            'user_id': obj.id,
            'latitude': obj.location.latitude,
            'longitude': obj.location.longitude
        })

    def decode(self, obj):
        """
        Decode a json string into Customer object

        Parameters
        ----------
        obj : str
            string with a json string

        Returns
        -------
        Customer
           customer object

        Raises
        ------
        JSONParserDecodeException
        """
        try:
            j = json.loads(obj)
            return Customer(
                id=j['user_id'],
                name=j['name'],
                latitude=j['latitude'],
                longitude=j['longitude']
            )
        except KeyError as e:
            raise JSONParserDecodeException(f'Error while decoding json: {e}')
