class Solution:
    def __init__(self) :
        self.successive_letter_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, 'u': 20}
    
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # from collections import defaultdict
        letter_position_dict = defaultdict(list)
        for string in strings : 
                    
            k = 0

            position_string = ''
            while k < len(string) - 1 : 
                current_letter_position = self.successive_letter_dict[string[k]]
                next_letter_position = self.successive_letter_dict[string[k+1]]
                diff = (next_letter_position - current_letter_position) % 26
                position_string = position_string + "_" + str(diff)
                
                k = k + 1
                
            letter_position_dict[position_string].append(string)
        
        
        return letter_position_dict.values()
            
