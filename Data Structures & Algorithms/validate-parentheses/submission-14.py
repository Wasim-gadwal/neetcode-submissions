class Solution:
    def isValid(self, s: str) -> bool:

        s_list = list(s)
        new = []

        for char in s_list:
            if char in '([{':
                new.append(char)
            elif char== ')' and new and new[-1] == '(' :
                new.pop()
            elif char == '}' and new and new[-1] == '{':
                new.pop()
            elif char == ']' and new and new[-1] == '[':
                new.pop()
            else:
                return False
            
        
        return len(new) == 0
       
       
                


            

                 



        