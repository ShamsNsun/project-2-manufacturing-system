class RawMaterial:
    def __init__(self, id):
        self.id = id

class IntermediatePart:
    def __init__(self, id):
        self.id = id

class FinishedProduct:
    def __init__(self, id):
        self.id = id

class Operation:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

class Machine:
    def __init__(self, id, operation, failure_rate):
        self.id = id
        self.operation = operation
        self.failure_rate = failure_rate

class Operator:
    def __init__(self, id, shift):
        self.id = id
        self.shift = shift
