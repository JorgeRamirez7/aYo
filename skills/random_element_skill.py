"""Gets a unique random element from a list."""
import random
from collections import deque

from utils.import_dialogue import ImportDialogue

class RandomElementSkill():
    def __init__(self, list):
        self.list = list
        self.add_random_elements_to_queue(self.dialogue)

    def add_random_elements_to_queue(self, list):
        self.stack = deque()
        
        for dialogue in list:
            stack.append(dialogue)

        print(self.stack)