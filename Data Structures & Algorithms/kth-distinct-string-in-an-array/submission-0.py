from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        a = []
        for key, val in count.items():
            if val == 1:
                a.append(key)
        if len(a) < k:
            return ""
        else:
            return a[k - 1]

        
        
        