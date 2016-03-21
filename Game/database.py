

def read_into_dict(level):
    """
      Function will return a dictionary. 
       The dictionary will contain the entire high-score
        list for the current level like this: 
         { Name1: [Points, Time-stamp, Duration, level, game],
           Name2: [Points, Time-stamp, Duration, level, game] }
           ....
           ----------------------------- Jonas ----      """
    file = open('Highscorelists\level{0}.txt'.format(level), 'r')
    
    highscore_dict = {} 
    while True:
        line_cache_raw = file.readline()               # Gets a string
        line_cache = line_cache_raw.replace("\\n", "") # Removes "\n" from string 
        line_list = line_cache.split(',')              # Makes string into list
        
        if line_cache == "":                           # This means end of file
            break
        else:
            #   DICTIONARY   [KEY]       = [VALUE1, VALUE2, VALUE3...]
            highscore_dict[line_list[0]] = line_list[1:]

    file.close()
    return highscore_dict


def write_from_dict(level, highscore_dict):
    """
      Function writes from the modified dictionary,
       back to the file in this format: 
        name,points,Time-stamp,Duration,level,game\n
        -------------------------- Jonas ----
       """
    file = open('Highscorelists\level{0}.txt'.format(level), 'w')
    while True: 
        try:
            item_pop = str(highscore_dict.popitem())
            #Format
            item_pop = item_pop.replace('"', '')
            item_pop = item_pop.replace('(', '')
            item_pop = item_pop.replace(')', '')
            item_pop = item_pop.replace('[', '')
            item_pop = item_pop.replace(']', '')
            item_pop = item_pop.replace('\'', '')
            item_pop = item_pop.replace(' ', '')
            
            file.write(item_pop)   
            file.write("\n")
        except KeyError:
            break

    file.close()
    return 0


def store_data(new_data):
    """ new_data is a list of:
    - user_name   index [0]
    - points      index [1]
    - time_stamp  index [2]
    - clock_diff  index [3]
    - level_int   index [4]
    - Game_name   index [5]
    ------------ Jonas ---"""
    level = new_data[4]     #Gets a integer between 1-4

    # read_into_dict() creates a dictionary from file-data
    highscore_dict = read_into_dict(level)
    # dictionary is modified with new data
    highscore_dict[new_data[0]] = [new_data[1:]]
    # The modified dictionary is written back to the file.
    write_from_dict(level, highscore_dict)







