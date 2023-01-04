class Solution:
    def sumEvenAfterQueries(self, nums,queries):
        answer=[]
        cur_sum=0
        for i in nums:
            if i%2==0:
                cur_sum += i
        for i in range(len(queries)):
            temp = nums[queries[i][-1]]
            nums[queries[i][-1]] = nums[queries[i][-1]] + queries[i][0]
            if temp%2 ==0 :
                if nums[queries[i][-1]] %2 == 0:
                    cur_sum += queries[i][0]
                else:
                    cur_sum -= temp
            else:
                if nums[queries[i][-1]] %2 == 0:
                    cur_sum += nums[queries[i][-1]]

            answer.append(cur_sum)
        return answer

