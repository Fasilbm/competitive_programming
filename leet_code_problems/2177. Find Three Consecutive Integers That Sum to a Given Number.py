class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans=[]
        if num%3==0:
            ans.append(int((num//3)-1))
            ans.append(int((num//3)))
            ans.append(int((num//3)+1))
            return ans
        else:
            return []

