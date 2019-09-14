import bisect
from geo_curator.parser import Customer, JSONParser


class CuratorJob:
    def __init__(self, reference, threshold, calculator, reader, writer, parser=JSONParser()):
        self.reference = reference
        self.threshold = threshold
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

            if distance <= self.threshold:
                bisect.insort(
                    self.sorted_list,
                    customer
                )

        for sorted_customer in self.sorted_list:
            self.writer.write(
                sorted_customer.to_str(self.parser)
            )
