"""
NAME:           Evan Whitmer
DATE:           10/9/2023
DESCRIPTION:    Write a function called find_anagrams which takes as input a list of words 
                and which returns a dictionary whose keys are these sorted strings and 
                whose values are lists of words that sort that way.
"""

my_animals =  ['cat','dog','stop','tops','god','spot', 'vase', 'save', 'tac'] #added a few more for good measure
thsDict = {}

def find_anagrams(a_list):
    a_dict = {}                                 #create an empty dictionary
    
    for a in a_list:                            #for position a in a list
        sorted_word = ''.join(sorted(list(a)))  #sorted word equals the current string sorted alphabetically
        if sorted_word not in a_dict:           #if the new word doesn't already exist in the dictionary as a key
            a_dict[sorted_word] = []            #add it as a new key
        a_dict[sorted_word].append(a)           #add the unsorted word to the list of items accompaning that key
                
    return a_dict

print(find_anagrams(my_animals))                #print the results