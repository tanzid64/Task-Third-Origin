class DictError(Exception):
    def __init__(self,key):
        self.key = key
    def __str__(self):
        return f'Key {self.key} does not exist in dict2'
    
class Dict2:
    def __init__(self):
        self.keys = []
        self.values = []

    def __setitem__(self,key,value):
        if key in self.keys:
            index = self.keys.index(key)
            self.values[index] = value
        else:
            self.keys.append(key)
            self.values.append(value)
    def __getitem__(self,key):
        if key in self.keys:
            index = self.keys.index(key)
            return self.values[index]
        else:
            raise DictError(key)
        
    def __iter__(self):
        return iter(self.keys)
    
# Test the functionality
obj = Dict2()
obj['a'] = 1
obj['b'] = 2
obj['c'] = 3

# Accessing values
try:
    print(obj['a'])
    print(obj['d'])  # This will raise a DictKeyError
except DictError as e: 
    print(e)

# Iterating over keys
for k in obj:
    print(f'key: {k}')