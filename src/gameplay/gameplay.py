import sys
import os
current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, "."))

import numpy as np
import pandas as pd

from .object import *
from .tile import *
from .rule import *

class Gameplay:
    def __init__(self, n_rows, n_cols):
        self.n_rows = n_rows
        self.n_cols = n_cols 
        self.prefixes = ['baba', 'rock', 'water', 'skull', 'wall', 'flag'] 
        self.suffixes = ['win', 'defeat', 'sink', 'you', 'push', 'stop']
        self.rules = []
        self.tiles = np.zeros((n_rows, n_cols), dtype=Tile) #chuot bach thay dtype=object bang tile
        for i in range(n_rows):
            for j in range(n_cols):
                self.tiles[i,j] = Tile() 
    
    def __repr__(self):
        ret_val = ''
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                tile_string = ''
                if len(self.tiles[i,j].objects) == 0:
                    tile_string += '/'
                    # tile_string += 'null'
                else:
                    for obj in self.tiles[i,j].objects:
                        if isinstance(obj, Word):
                            tile_string += obj.value.upper() 
                        else:
                            tile_string += obj.property if obj.property !='' else 'null'
                        tile_string += ','
                ret_val += '{:10}'.format(tile_string)
                # ret_val += tile_string
            ret_val += '\n'           
        return ret_val

    def get_rules(self):
        self.rules = []
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if self.tiles[i,j].find_word() == 'is':
                    if j-1 >= 0 and j+1 <= self.n_cols-1:
                        if self.tiles[i,j-1].find_word() in self.prefixes and self.tiles[i,j+1].find_word() in self.suffixes:
                            self.rules += [Rule(self.tiles[i,j-1].find_word(),self.tiles[i,j+1].find_word())]
                    if i-1 >= 0 and i+1 <= self.n_rows-1:
                        if self.tiles[i-1,j].find_word() in self.prefixes and self.tiles[i+1,j].find_word() in self.suffixes:
                            self.rules += [Rule(self.tiles[i-1,j].find_word(),self.tiles[i+1,j].find_word())]
    
    def apply_rules(self):
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                tile = self.tiles[i,j]
                for obj in tile.objects:
                    if obj.name != 'word':
                        obj.property = ''
                        for rule in self.rules:
                            if obj.name == rule.first:
                                obj.property = rule.second


    # find a block upward (continuous)
    # return block size if the block can be moved up
    # return -1 if the block is blocked
    def find_up_block(self, r, c):
        if not self.tiles[r,c].have_property('you'):
            return 0
        
        current_row = r - 1 #dem row tu 0 nen phai -1
        count = 1

        if current_row < 0: #khong day block len duoc nua
            return -1

        while current_row >= 0 and self.tiles[current_row,c].have_property('push'): #trong truong hop day duoc block thi dem row
            count += 1
            current_row -= 1
        
        if current_row < 0  or self.tiles[current_row,c].have_property('stop') or self.tiles[current_row,c].have_property('you'): #check o tiep theo cua block co phai limit cua map hoac chua stop hay khong
            return -1
        else:
            return count

    def find_down_block(self, r, c):
        if not self.tiles[r,c].have_property('you'):
            return 0
        
        current_row = r + 1 
        count = 1

        if current_row >= self.n_rows: 
            return -1

        while current_row < self.n_rows and self.tiles[current_row,c].have_property('push'): 
            count += 1
            current_row += 1
        
        if current_row >= self.n_rows or self.tiles[current_row,c].have_property('stop') or self.tiles[current_row,c].have_property('you'): 
            return -1
        else:
            return count    

    def find_left_block(self, r, c):
        if not self.tiles[r,c].have_property('you'):
            return 0
        
        current_col = c - 1 #dem row tu 0 nen phai -1
        count = 1

        if current_col < 0: #khong day block len duoc nua
            return -1

        while current_col >= 0 and self.tiles[r,current_col].have_property('push'): #trong truong hop day duoc block thi dem row
            count += 1
            current_col -= 1
        
        if current_col < 0  or self.tiles[r,current_col].have_property('stop') or self.tiles[r,current_col].have_property('you'): #check o tiep theo cua block co phai limit cua map hoac chua stop hay khong
            return -1
        else:
            return count

    def find_right_block(self, r, c):
        if not self.tiles[r,c].have_property('you'):
            return 0
        
        current_col = c + 1 
        count = 1

        if current_col >= self.n_cols: 
            return -1

        while current_col < self.n_cols and self.tiles[r,current_col].have_property('push'): 
            count += 1
            current_col += 1
        
        if current_col >= self.n_cols or self.tiles[r,current_col].have_property('stop') or self.tiles[r,current_col].have_property('you'): 
            return -1
        else:
            return count   

    def move_up(self):  
        for r in range(self.n_rows):
            for c in range(self.n_cols):
                size = self.find_up_block(r,c)
                if size > 0:
                    for current_row in range(r - size + 1, r + 1):
                        temp = self.tiles[current_row,c].pop_push_or_you()
                        # self.tiles[current_row-1,c].objects = np.append(self.tiles[current_row-1,c].objects,[temp])
                        self.tiles[current_row-1,c].add_object(temp)


    def move_down(self):
        for r in range(self.n_rows-1, -1, -1):
            for c in range(self.n_cols):
                size = self.find_down_block(r,c)
                if size > 0:
                    for current_row in range(r + size - 1, r - 1, -1):
                        temp = self.tiles[current_row,c].pop_push_or_you()
                        # self.tiles[current_row+1,c].objects = np.append(self.tiles[current_row+1,c].objects,[temp])
                        self.tiles[current_row+1,c].add_object(temp)
        

    def move_left(self):
        for c in range(self.n_cols):
            for r in range(self.n_rows):
                size = self.find_left_block(r,c)
                if size > 0:
                    for current_col in range(c - size + 1, c + 1):
                        temp = self.tiles[r,current_col].pop_push_or_you() #luu o hien tai vao 1 bien tam thoi
                        # self.tiles[r,current_col-1].objects = np.append(self.tiles[r,current_col-1].objects,[temp]) #dan vao o tiep theo
                        self.tiles[r,current_col-1].add_object(temp)
        

    def move_right(self):
        for c in range(self.n_cols-1, -1, -1):
            for r in range(self.n_rows):
                size = self.find_right_block(r,c)
                if size > 0:
                    for current_col in range(c + size - 1, c - 1, -1):
                        temp = self.tiles[r,current_col].pop_push_or_you()
                        # self.tiles[r,current_col+1].objects = np.append(self.tiles[r,current_col+1].objects,[temp])
                        self.tiles[r,current_col+1].add_object(temp)
        

    def check_win(self):
        for r in range(self.n_rows):
            for c in range(self.n_cols):
                if self.tiles[r,c].have_property('you') and self.tiles[r,c].have_property('win'):
                    return True
        return False

    def check_lose(self):
        for r in range(self.n_rows):
            for c in range(self.n_cols):
                if self.tiles[r,c].have_property('you'):
                    return False
        return True

    def reset_game(self):
        self.load_map(self.map_file,self.info_file)
        pass

    def load_map(self, map_file, info_file):
        self.map_file = map_file
        self.info_file = info_file
        with open(info_file) as f:
            self.n_rows = int(f.readline())
            self.n_cols = int(f.readline())
        self.rules = []
        self.tiles = np.zeros((self.n_rows, self.n_cols), dtype=Tile) #reset va resize cho vua info file
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                self.tiles[i,j] = Tile() 
        map_data = pd.read_csv(map_file, header = None, sep = ';')
        map_array = np.array(map_data, dtype = str)
        for r in range(self.n_rows):
            for c in range(self.n_cols):
                value_data = map_array[r,c].split('/')
                for value in value_data:
                    if value == '':
                        continue
                    elif value == 'baba':
                        self.tiles[r,c].add_object(Baba())
                    elif value == 'rock':
                        self.tiles[r,c].add_object(Rock())
                    elif value == 'water':
                        self.tiles[r,c].add_object(Water())
                    elif value == 'skull':
                        self.tiles[r,c].add_object(Skull())
                    elif value == 'wall':
                        self.tiles[r,c].add_object(Wall())
                    elif value == 'flag':
                        self.tiles[r,c].add_object(Flag())
                    elif value.isupper():
                        self.tiles[r,c].add_object(Word(value.lower()))   