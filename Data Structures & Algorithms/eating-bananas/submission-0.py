class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k = bananas-per-hour
        # h = parameter of hours
        # piles = pile of bananas
        # piles[i] = number of bananas in the ith pile
        left = 1
        right = max(piles)
        total_hours = 0
        k = 0
        while (left <= right):
            k = (left + right) // 2
            total_hours = 0

            for pile in piles:
                total_hours += (k + pile - 1) // k

            if total_hours <= h:
                right = k - 1
            else:
                left = k + 1
        return left