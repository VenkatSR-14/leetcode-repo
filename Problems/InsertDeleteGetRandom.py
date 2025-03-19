import random

class RandomizedSet:
    
    def __init__(self):
        self.hashmap = {}
        self.array = []
    
    def insert(self, value):
        if value not in self.hashmap:
            self.hashmap[value] = len(self.array)
            self.array.append(value)
            return True
        else:
            return False
    
    def remove(self, val):
        if val not in self.hashmap:
            return False
        last_element = self.array[-1]
        curr_idx = self.hashmap[val]
        self.hashmap[last_element] = curr_idx
        self.array[curr_idx] = last_element
        del self.hashmap[val]
        return True
    
    def get_random(self):
        return random.choice(self.array)
