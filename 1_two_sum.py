class Solution:
    def twoSum_sort(self, nums: List[int], target: int) -> List[int]:
      return twoSum_dict(nums, target)
    # with sort and double pointer
    def twoSum_sort(self, nums: List[int], target: int) -> List[int]:
      nums_index = [(v, idx) for idx, v in enumerate(nums)]
      nums_index.sort()
      l,r = 0, len(nums_index)-1
      while (r>l):
        sum = nums_index[l][0] + nums_index[r][0]
        if sum == target:
          return [nums_index[l][1],nums_index[r]]
        if sum > target:
          r = r-1
        if sum < target:
          l = l+1 
    
    # with dict (lookup is O(1) for small collisions
    def twoSum_dict(self, nums: List[int], target: int) -> List[int]:
        nums_index = {v: idx for idx, v in enumerate(nums)}
                
        for idx, n in enumerate(nums):
          complement = target - n            
          if complement in nums_index and nums_index[complement] != idx:
            return [idx, nums_index[complement]]
        return []
