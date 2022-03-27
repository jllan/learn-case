from typing import List

class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums, start=0, path=[]):
            if not nums:
                res.append(path[:])
                return 
            for i in range(len(nums)):
                path.append(nums[i])
                dfs(nums[:i]+nums[i+1:], i, path)
                path.pop()
        dfs(nums[:])
        return res



class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used):
            if depth == size:
                res.append(path[:])
                return

            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    dfs(nums, size, depth + 1, path, used)

                    used[i] = False
                    path.pop()

        size = len(nums)
        if len(nums) == 0:
            return []

        used = [False for _ in range(size)]
        res = []
        dfs(nums, size, 0, [], used)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution1()
    res = solution.permute(nums)
    print(res)
