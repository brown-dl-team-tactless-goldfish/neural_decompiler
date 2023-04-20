class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ans = 0 
        prefix = least = customers.count('Y')
        for i, ch in enumerate(customers): 
            if ch == 'N': prefix += 1
            else: prefix -= 1; 
            if prefix < least: 
                ans = i+1
                least = prefix 
        return ans 