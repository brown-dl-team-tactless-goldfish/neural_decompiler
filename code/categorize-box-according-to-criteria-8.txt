class Solution:
    def categorizeBox(self, l: int, w: int, h: int, m: int) -> str:
        k,b1,b2,v = 10**4, 0, 0, l*w*h
        if l>=k or w>=k or h>=k or v>=10**9: b1 = 1
        if m>=100: b2 = 1
        if b1+b2==2: return "Both"
        if b1+b2==0: return "Neither"
        return "Bulky" if b1==1 else "Heavy"