import argparse    
import os 


def find_all_anagrams(filename):
    # original data from txt file
    lst_of_words = []
    anagram_lst = []   
    
    # Opening up the txt file so that I can interact with the data
    file = open(filename) 
    # Looping through each word in the list
    for word in file.readlines():  
        words = word.strip()
        # Storing each word in a list
        lst_of_words.append(words)
            
        # Looping through the list to try and identify anagrams
        for index, word1 in enumerate(lst_of_words):
            for word2 in lst_of_words[index + 1:]:
                if len(word1) == len(word2) and sorted(word1.lower()) == sorted(word2.lower()):
                    # Identified anagrams are now appended to the anagram_lst
                    anagram_lst.append(" ".join([word1, word2]))    
                    # Duplicate data is removed from the list
                    anagram_lst = list(dict.fromkeys(anagram_lst))  
                    
        # List comprehension and split used to compare the anagram list and original data             
        anagram_lst_split_str = [each_word for word in anagram_lst for each_word in word.split()]
        # List comprehnsion used to identify the words that are not an anagram
        non_anagram_lst = [word for word in lst_of_words if word not in anagram_lst_split_str]
        # Created a final lst to show both anagrams and non anagrams
        lst_with_anagram_paired = anagram_lst + non_anagram_lst
                   
    return lst_with_anagram_paired
                            
    file.close()                                
            


def write_to_file(filename, result):
    # Opening the file in write mode
    with open(filename, 'w') as f:  # Open file in write mode
        for line in result:
            # Each word will be represented on a seperate line
            f.write(line + "\n")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Find and group anagrams from a list of words")
    parser.add_argument("filename", type = str, help = "Name of the file containing the list of words" )
    args = parser.parse_args()
    directory = r"C:\Users\jj_jo\Documents"
    full_path = os.path.join(directory, args.filename)
    result = find_all_anagrams(full_path)
    write_to_file(full_path, result)
            


