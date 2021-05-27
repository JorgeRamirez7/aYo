"""Gets a unique random element from a list."""
import random
from collections import deque

from utils.import_dialogue import ImportDialogue

class RandomElementSkill():
    def __init__(self, list):
        self.list = list
        random_stack = self.add_random_elements_to_stack(self.list)
        self.stack = random_stack

    def add_random_elements_to_stack(self, list):
        elements_stack = deque()
        
        while list:
            random_element = random.choice(list)
            elements_stack.append(random_element)
            list.remove(random_element)

        return elements_stack

    def get_random_element(self):
        if not self.stack:
            self.add_random_elements_to_stack(self.list)
            
        element = self.stack.pop()
        return element
