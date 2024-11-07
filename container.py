import pickle

class Container:
    def __init__(self, content=None):
        self.empty = content is None
        self._content = content

    def get(self):
        return self._content
    
    def put(self, content):
        if not self.empty:
            raise ValueError("Container is not empty!")
        self._content = content
        self.empty = True
    
    def clear(self):
        self._content = None
        self.empty = True

class EncryptedContainer:
    def __init__(self):
        self.empty = True
        self._content = None
        self._key = None
    
    def put(self, content, key):
        self.empty = content is not None
        self._content = pickle.dumps(content)