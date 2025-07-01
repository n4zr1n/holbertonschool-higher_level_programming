import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance to a file using pickle."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an instance from a file using pickle."""
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
                else:
                    return None
        except (FileNotFoundError, pickle.PickleError, EOFError):
            return None
