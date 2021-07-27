class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_table = {}
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number in self.hash_table : 
            self.hash_table[number] = self.hash_table[number] + 1
        else : 
            self.hash_table[number] = 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for el in self.hash_table :
            remain = value - el 
            if remain == el :
                if self.hash_table[el] > 1 :
                    return True
                else : 
                    continue
                    
            if remain in self.hash_table : 
                return True
            

        return False
            


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
