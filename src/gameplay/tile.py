import numpy as np
import pandas as pd

from .object import *

class Tile:
    def __init__(self):
        self.objects = np.array([], dtype=object)

    def add_object(self, new_obj : Object):
        has_interacted = False
        obj_after_interaction = []
        for obj in self.objects:
            if has_interacted or obj.interact(new_obj) == None:
                obj_after_interaction = np.append(obj_after_interaction, [obj])
            else:
                obj_after_interaction = np.append(obj_after_interaction, obj.interact(new_obj))
                has_interacted = True
        
        self.objects = obj_after_interaction

        if not has_interacted:
            self.objects = np.append(self.objects,[new_obj])

    def find_word(self):
        for obj in self.objects:
            if isinstance(obj, Word):
                return obj.value
        return ''
    
    def pop_push_or_you(self):
        position = -1
        for i in range(len(self.objects)):
            if self.objects[i].property == 'push' or self.objects[i].property == 'you':
                position = i
        temp_object = self.objects[position]
        self.objects = np.delete(self.objects, position)
        return temp_object       

    def have_property(self,property):
        for obj in self.objects:
            if obj.property == property:
                return True
        return False
    
    def __repr__(self):
        s = ''
        for obj in self.objects:
            s += obj.name + ',' + obj.property + '/'
        return s
    