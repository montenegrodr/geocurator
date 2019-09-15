import bisect
import logging
from geo_curator.parser import Customer

logger = logging.getLogger('geo_curator')


class CuratorJob:
    """
    Curates elements from an source based on the distance from a reference location
    """
    def __init__(self, reference, radius, calculator, reader, writer, parser):
        """
        Parameters
        ----------
        reference : geo_curator.parser.Location
            reference location
        radius : float
            distance threshold
        calculator : geo_curator.distance.DistanceCalculator
            distance calculator method
        reader : geo_curator.io.Reader
            input source
        writer : geo_curator.io.Writer
            output
        parser : geo_curator.parser.Parser
            object encoder/decoder
        """

        self.reference = reference
        self.radius = radius
        self.calculator = calculator
        self.reader = reader
        self.writer = writer
        self.parser = parser
        self.sorted_list = []

    def run(self):
        """
        Curates elements from reader and publish on writer
        """
        for customer_str in self.reader.iterator():
            customer = Customer.from_str(customer_str, self.parser)
            distance = self.calculator.distance(
                self.reference,
                customer.location
            )

            if distance <= self.radius:
                # Insert customer in sorted list
                # and keep it sorted O(log n)
                bisect.insort(
                    self.sorted_list,
                    customer
                )

        for sorted_customer in self.sorted_list:
            customer_str = sorted_customer.to_str(self.parser)
            self.writer.write(customer_str)
            logger.info(customer_str)
