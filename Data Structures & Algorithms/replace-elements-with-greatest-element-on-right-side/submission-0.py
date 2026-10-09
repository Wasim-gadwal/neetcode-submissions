class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        prev = 0
        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr) - 1:
                res[i] = -1
                prev = max(prev, arr[i])
            else:
                prev = max(prev, arr[i+1])
                res[i] = prev
        return res


