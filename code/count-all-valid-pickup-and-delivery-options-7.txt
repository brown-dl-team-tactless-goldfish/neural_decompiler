from functools import reduce
from operator import mul
class Solution:
    def countOrders(self, n: int) -> int:
        return reduce(mul, (*range(1,n+1), *range(1,2*n,2)), 1) % (10**9+7)