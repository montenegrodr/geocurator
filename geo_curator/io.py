import codecs

DEFAULT_ENCODING = 'utf-8'


class Reader:
    def iterator(self):
        raise NotImplementedError()


class TextFileReader(Reader):
    def __init__(self, file_path):
        self.file_path = file_path

    def iterator(self):
        with codecs.open(filename=self.file_path,
                         encoding=DEFAULT_ENCODING) as r:
            for line in r:
                yield line


class Writer:
    def write(self, line):
        raise NotImplementedError()


class TextFileWriter(Writer):
    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, line):
        with codecs.open(filename=self.file_path,
                         encoding=DEFAULT_ENCODING,
                         mode='a') as w:
            w.write(line + '\n')
