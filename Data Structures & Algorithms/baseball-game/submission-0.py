class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for ope in operations:
            if ope == '+':
                eml = stk[-1] + stk[-2]
                stk.append(int(eml))
            elif ope == 'C':
                stk.pop()
            elif ope == 'D':
                eml = stk[-1]
                stk.append(int(eml*2))
            else:
                stk.append(int(ope))
        
        return sum(stk)

        