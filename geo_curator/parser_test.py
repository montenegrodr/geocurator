import unittest
from geo_curator.parser import Customer, JSONParser


class TestParser(unittest.TestCase):

    def setUp(self):
        self.id = 12
        self.name = 'Chris'
        self.latitude = 52.986375
        self.longitude = -6.043701

        self.cus_str = """
        {
            "user_id": %s,
            "name": "%s",
            "latitude": "%s",
            "longitude": "%s"
        }
        """ % (self.id,
               self.name,
               self.latitude,
               self.longitude)

        self.cus_obj = Customer(id=self.id,
                                name=self.name,
                                latitude=self.latitude,
                                longitude=self.longitude)

    def test_customer_encoding(self):
        cus_obj = Customer.from_str(self.cus_str, JSONParser())
        assert cus_obj.id == self.id, \
            "Customer id incorrectly decoded"
        assert cus_obj.name == self.name, \
            "Customer name incorrectly decoded"
        assert cus_obj.location().latitude == self.latitude, \
            "Customer latitude incorrectly decoded"
        assert cus_obj.location().longitude == self.longitude, \
            "Customer longitude incorrectly decoded"

    def test_customer_decoding(self):
        assert self.cus_obj.to_str(JSONParser()) == self.cus_str, \
            "Customer incorrectly decoded"
