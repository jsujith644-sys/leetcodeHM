class Solution(object):
    def guessNumber(self, n):
        l, r, check = 1, n, 1
        while check != 0:
            mid = (l + r) / 2
            check = guess(mid)
            if check == 1: l = mid + 1
            else: r = mid - 1
        return mid