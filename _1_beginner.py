
def lets_roll():
    #Strings and arrays
    word = "hi how are you?"
    size = len(word)
    arr = [1,2,"helo", [2,3,4], 5]
    size = len(arr)

    #SETS
    my_set = set()
    my_set = {1, 2, 3}
    for val in my_set:
        pass #iterating over set

    #dictionary
    my_dict = {}
    my_dict["keyyy"]="valueee"
    size = len(my_dict)
    keys = my_dict.keys()
    values = my_dict.values()


    for key in my_dict:
        pass

    for key, value in my_dict.items():
        #print(key, '->', value)
        pass

if __name__ == "__main__":
    lets_roll()
