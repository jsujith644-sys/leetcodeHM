class Solution(object):
    def twoSum(self, numbers, target):
        x = 0
        i = len(numbers)-1
        while x < i:
                    current_sum = numbers[i] + numbers[x]
                    if target < current_sum:
                                            i -= 1
                    elif target > current_sum:
                                              x +=1
                    else:
                         return x +1, i+1
                        