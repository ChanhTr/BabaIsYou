import numpy as np
import pandas as pd

class Rule:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def __repr__(self):
        return self.first + " is " + self.second
            