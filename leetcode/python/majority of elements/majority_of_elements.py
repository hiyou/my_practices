class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        num.sort()
        n = len(num)
        return num[n / 2]