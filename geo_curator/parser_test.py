import unittest
from geo_curator.parser import Customer, JSONParser, JSONParserDecodeException


class TestParser(unittest.TestCase):

    def setUp(self):
        self.id = 12
        self.name = 'Chris'
        self.latitude = 52.986375
        self.longitude = -6.043701

        self.cus_str = """
        {
            "name": "%s",
            "user_id": %s,
            "latitude": "%s",
            "longitude": "%s"
        }
        """ % (self.name,
               self.id,
               self.latitude,
               self.longitude)

        self.cus_obj = Customer(id=self.id,
                                name=self.name,
                                latitude=self.latitude,
                                longitude=self.longitude)

    def test_customer_json_encoding(self):
        cus_obj = Customer.from_str(self.cus_str, JSONParser())
        assert cus_obj.id == self.id, \
            "Customer id incorrectly decoded"
        assert cus_obj.name == self.name, \
            "Customer name incorrectly decoded"
        assert cus_obj.location.latitude == self.latitude, \
            "Customer latitude incorrectly decoded"
        assert cus_obj.location.longitude == self.longitude, \
            "Customer longitude incorrectly decoded"

    def test_customer_json_decoding(self):
        assert self.cus_obj.to_str(JSONParser()) == \
               '{"name": "%s", ' \
               '"user_id": %s, ' \
               '"latitude": %s, ' \
               '"longitude": %s}' \
               % (self.name,
                  self.id,
                  self.latitude,
                  self.longitude), "Customer incorrectly decoded"

    def test_missing_field_json_encoding(self):
        cus_str_missing_field = """
        {
            "user_id": %s,
            "latitude": "%s",
            "longitude": "%s"
        }
        """ % (self.id,
               self.latitude,
               self.longitude)
        with self.assertRaises(JSONParserDecodeException):
            Customer.from_str(cus_str_missing_field, JSONParser())

    def test_empty_json_encoding(self):
        with self.assertRaises(JSONParserDecodeException):
            Customer.from_str('{}', JSONParser())

