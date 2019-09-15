import codecs

DEFAULT_ENCODING = 'utf-8'


class Reader:
    """
    Abstract class for input reader
    """
    def iterator(self):
        raise NotImplementedError()


class TextFileReader(Reader):
    def __init__(self, file_path):
        """
        Parameters
        ----------
        file_path : str
            absolute file path
        """
        self.file_path = file_path

    def iterator(self):
        """
        Returns a generator with lines within `file_path`
        Returns
        -------
         Iterator[str]
            lines of `file_path`
        """
        with codecs.open(filename=self.file_path,
                         encoding=DEFAULT_ENCODING) as r:
            for line in r:
                yield line


class Writer:
    """
    Abstract class for writer
    """
    def write(self, line):
        raise NotImplementedError()


class TextFileWriter(Writer):
    def __init__(self, file_path):
        """
        Parameters
        ----------
        file_path : str
            absolute file path
        """
        self.file_path = file_path

    def write(self, line):
        """
        Append `line` to `file_path`

        Parameters
        ----------
        line : str
            new line to write
        """
        with codecs.open(filename=self.file_path,
                         encoding=DEFAULT_ENCODING,
                         mode='a') as w:
            w.write(line + '\n')
