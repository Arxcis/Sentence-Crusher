#!/usr/bin/env python
# coding: utf-8

import os
import pickle


class StorageGuy:
    """ This class reads from, and writes to files, and sends data to server"""
    def __init__(self):
        print("StorageGuy initialized")

    def store_data(self, data):
        """ Tasks:
            1. Compare old data vs new data
            2. Store new data if old points is worse, or 
                non-existent.
        ------------------------ Jonas ---"""
        # --- Get data.level_history ----
        data.level_history = self.read_from_file(data.level)
        # Task 1
        try: 
            old_points = int(data.level_history[data.user][0])
        except KeyError:
            old_points = 0
        
        if data.points > old_points:
            # Task 2    
            data.generate_newdata_list()
            data.level_history[data.user] = data.new_data

            self.write_to_file(data.level_history, data.level)
            data.new_is_better = True
        else: 
            pass

    def read_from_file(self, level):
        """ Function returns a dictionary containing
             previous records for the current level.
              Format: 
             { Name1: [Points, Username, Time-stamp, Duration, level, game],
               Name2: [Points, Username, Time-stamp, Duration, level, game] }
               ....
               ---------------------------------  """
        with open(self.init_levelfile(level), 'rb') as f:
            return pickle.load(f)

    def write_to_file(self, records, level):
        """Function dumps the dictionary containing 
            up to date current-level records, to 
             a level-specific file.   
              ---------------------------- """
        with open(self.init_levelfile(level), 'wb') as f:
            pickle.dump(records, f)

    def init_levelfile(self, level):
        return os.path.join(os.path.dirname(__file__),('levelrecords/level{0}.pickle'.format(level)))


# ---- For Debugging ------------
if __name__ == "__main__":
    storage = StorageGuy()

    new = {'Bottom line': ['0', 'trololol']}

    for level in range(1, 5):
        storage.write_to_file(new, level)

    for level in range (1, 5):
        cache = storage.read_from_file(level)
        print(cache)
