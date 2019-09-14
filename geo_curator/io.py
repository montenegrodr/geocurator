import codecs

DEFAULT_ENCODING = 'utf-8'


class Reader:
    def __iter__(self):
        return self

    def __next__(self):
        raise NotImplementedError()


class TextFileReader(Reader):
    def __init__(self, file_path):
        self.handle = codecs.open(
            file_name=file_path,
            encoding=DEFAULT_ENCODING
        )

    def __next__(self):
        try:
            for line in self.handle:
                return line
        finally:
            self.handle.close()
            raise StopIteration


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
