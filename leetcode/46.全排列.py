class Solution:
    def permute(self, nums):
        def backtrack(nums, tem):
            if nums == []:
                if tem not in res:
                    res.append(tem[:])
            else:
                for i in range(len(nums)):
                    tem.append(nums[i])
                    backtrack(nums[0:i] + nums[i + 1:], tem)
            if tem == []:
                return
            tem.pop()

        res = []
        tem = []
        backtrack(nums, tem)
        return res


s = Solution()
res = s.permute([1, 2, 3])
print(res)
