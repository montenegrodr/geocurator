import bisect
import logging
from geo_curator.parser import Customer, JSONParser

logger = logging.getLogger('geo_curator')


class CuratorJob:
    def __init__(self, reference, radius, calculator, reader, writer, parser):
        self.reference = reference
        self.radius = radius
        self.calculator = calculator
        self.reader = reader
        self.writer = writer
        self.parser = parser
        self.sorted_list = []

    def run(self):
        for customer_str in self.reader.iterator():
            customer = Customer.from_str(customer_str, self.parser)
            distance = self.calculator.distance(
                self.reference,
                customer.location
            )

            if distance <= self.radius:
                bisect.insort(
                    self.sorted_list,
                    customer
                )

        for sorted_customer in self.sorted_list:
            customer_str = sorted_customer.to_str(self.parser)
            self.writer.write(customer_str)
            logger.info(customer_str)
