class Solution(object):
    def largestAltitude(self, gain):
        arr=[0];
        for i in gain:
            arr.append(arr[-1]+i);
        return max(arr)
        """
        :type gain: List[int]
        :rtype: int
        """
        