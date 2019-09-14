import os
import unittest

from geo_curator.distance import GreatCircle
from geo_curator.curator import CuratorJob
from geo_curator.io import TextFileReader, Writer, TextFileWriter
from geo_curator.parser import Location


def fixture(file_name):
    return os.path.join(os.path.dirname(__file__), f'fixtures/{file_name}.txt')


class MockWriter(Writer):
    def __init__(self):
        self.mock_file = []

    def write(self, line):
        self.mock_file.append(line)


class TestJob(unittest.TestCase):

    def setUp(self):
        self.radius = 100
        self.calculator = GreatCircle()
        self.reference = Location(53.339428, -6.257664)
        self.writer = MockWriter()

    def test_text_file_reader(self):
        CuratorJob(radius=self.radius,
                   reference=self.reference,
                   calculator=self.calculator,
                   writer=self.writer,
                   reader=TextFileReader(fixture('test_job_customers'))
                   ).run()

        assert len(self.writer.mock_file) == 4, \
            'Incorrect number of customers.'

    def test_file_not_found_reader(self):
        with self.assertRaises(FileNotFoundError):
            CuratorJob(radius=self.radius,
                       reference=self.reference,
                       calculator=self.calculator,
                       writer=self.writer,
                       reader=TextFileReader(fixture(''))
                       ).run()

    def test_file_not_found_writer(self):
        with self.assertRaises(FileNotFoundError):
            CuratorJob(radius=self.radius,
                       reference=self.reference,
                       calculator=self.calculator,
                       writer=TextFileWriter(''),
                       reader=TextFileReader(fixture('test_job_customers'))
                       ).run()
