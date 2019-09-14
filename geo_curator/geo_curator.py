class Job:
    def __init__(self, calculator, reader, writer):
        self.calculator = calculator
        self.reader = reader
        self.writer = writer

    def run(self):
        raise NotImplementedError()
