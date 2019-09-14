import codecs


class Reader:
    def __iter__(self):
        return self

    def __next__(self):
        raise NotImplementedError()


class TextFileReader(Reader):
    def __init__(self, file_path):
        self.file_path = file_path

    def __next__(self):
        with codecs.open(self.file_path, encoding='utf-8') as _:
            raise StopIteration
        # raise NotImplementedError()


class Writer:
    def write(self, obj):
        raise NotImplementedError()


class TextFileWriter(Writer):
    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, obj):
        raise NotImplementedError()
