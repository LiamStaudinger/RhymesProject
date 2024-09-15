'''
File: rhymes.py
Author: Liam Staudinger
Course: CSC 120, Spring 2024
Purpose: This program processes a file containing information 
    about words and their rhymes. It builds a dictionary of rhymes 
    and then responds to a set of queries about the rhymes. It answers 
    the queries by printing the words that rhyme with the input word. 
'''
def open_file():
    '''
    Open a file and build a dictionary of rhymes.
  
    Parameters:
    - None
  
    Returns: 
    - A dictionary where the keys are words and the values are lists 
      of lists, each containing the rhymes for the key word.
    '''
    pfile = input()
    rhyme_dict = {}
    # Open the file and read its contents
    pfile_contents = open(pfile)
    for line in pfile_contents:
        # Split each line into phonemes 
        line = line.strip().split(' ')
        rhyme_list = []
        # Build a list of phoneme data for each word
        for i in range(len(line)):
            if i != 0 and line[i] != '':
                rhyme_list.append(line[i])
        # Add the word and its phoneme data list to the dictionary
        if line[0] not in rhyme_dict:
            rhyme_dict[line[0]] = [rhyme_list]
        elif line[0] in rhyme_dict:
            rhyme_dict[line[0]].append(rhyme_list)
    pfile_contents.close()
    return rhyme_dict
                                                                            
def find_rhymes(rhyme_dict):
    '''
    FindS words that rhyme with the input word.
  
    Parameters: 
    - rhyme_dict is a dictionary where the keys are words and the 
      values are lists of lists, each containing the rhymes for the key word.
  
    Returns: 
    - A list of words that rhyme with the input word.
    '''
    word  = input()
    rhyme_data  = rhyme_dict[word.upper()]
    found_rhymes = []
    perfect_data = []
    # Iterate over all of the rhyme data for the input word
    for i in range(len(rhyme_data)):
        for j in range(len(rhyme_data[i])):
            # Identify primmary stress, preceding, and subsequent sounds
            if '1' in rhyme_data[i][j]:
                primary_stress = rhyme_data[i][j]
                subsequent_sound_list = rhyme_data[i][j + 1:]
                preceding_sound = rhyme_data[i][j-1]
                subsequent_sound = ''.join(subsequent_sound_list)
                sounds_list = []
                # Append each possible pronunciatin of the input word to a list 
                # of lists
                sounds_list.append(preceding_sound)
                sounds_list.append(primary_stress)
                sounds_list.append(subsequent_sound)
                perfect_data.append(sounds_list)
    # Compare all of those sounds with those of each word in the dictionary
    for key, value in rhyme_dict.items():
        for innerlist in value:
            for i in range( len(innerlist)):
                if '1' in innerlist[i]:
                    primary_stress_hold = innerlist[i]
                    subsequent_sound_hold_list = innerlist[i + 1:]
                    preceding_sound_hold = innerlist[i - 1] 
                    subsequent_sound_hold = ''.join(subsequent_sound_hold_list)
                    sounds_list_hold = []
                    sounds_list_hold.append(preceding_sound_hold)
                    sounds_list_hold.append(primary_stress_hold)
                    sounds_list_hold.append(subsequent_sound_hold)
                    # Iterate through each pronunciation of the input word
                    for sublist in perfect_data:
                        # If the sounds match, add the word to a list of found 
                        # rhymes
                        if sublist[0] != sounds_list_hold[0]:
                            if sublist[1] == sounds_list_hold[1]:
                                if sublist[2] == sounds_list_hold[2]:
                                    if key.lower() != word.lower():
                                        found_rhymes.append(key)
    return found_rhymes    
  
def main():
    '''
    Main function to run the program.
  
    Parameters: 
    - None
  
    Returns: 
    - None
    '''
    rhyme_dict = open_file()
    found_rhymes = find_rhymes(rhyme_dict)
    # Print rhymes in alphabetical order
    for value in sorted(found_rhymes):
        print(value)
main()