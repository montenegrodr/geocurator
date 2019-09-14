import unittest
from unittest import mock
from geo_curator.io import TextFileReader, TextFileWriter


class TestIO(unittest.TestCase):
    @mock.patch('geo_curator.io.codecs')
    def test_text_file_reader(self, mock_codecs):
        for _ in TextFileReader('').iterator():
            pass
        self.assertTrue(mock_codecs.open.called)

    @mock.patch('geo_curator.io.codecs')
    def test_text_file_writer(self, mock_codecs):
        TextFileWriter('').write('')
        self.assertTrue(mock_codecs.open.called)
        self.assertTrue(mock_codecs.open.return_value.__enter__.return_value
                        .write.called)
