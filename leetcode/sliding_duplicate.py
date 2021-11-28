class Solution:
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

      # # Brute force O(n^2) 
      # for i, numi in enumerate(nums):
      #     for j, numj in enumerate(nums):
      #         if i == j:
      #             continue
      #         if numi == numj and abs(i - j) <= k:
      #             return True
      # return False

      # # Faster O(nlogn)
      # for i, numi in enumerate(nums):
      #     for j in range(i+1, len(nums)):
      #         if not numi == nums[j]:
      #             continue
      #         if abs(i - j) <= k:
      #             return True
      # return False

      # use built-ins

      # # More Confusing
      # for i, numi in enumerate(nums):
      #     try:
      #         j = nums[i:].index(numi)
      #     except ValueError:
      #         continue
      #     if abs(i - j) <= k:
      #         return True
      # return False

      # Lean more into the value of k

      # # Sliding window O(k*n)
      # for i, numi in enumerate(nums):
      #     for numj in nums[i+1:i+k+1]:
      #         if numi == numj:
      #             return True
      # return False

      # Avoid enumerate and slicing

      # # Sliding window O(k*n)
      # for i in range(len(nums)):
      #     for j in range(i+1, min(len(nums), i+k+1)):
      #         if nums[i] == nums[j]:
      #             return True
      # return False

      # Add condition for list size of 1
      if len(nums) <= 1:
          return False

      # Add conditions for k of zero
      if k == 0:
          return False

      # Add condition for large k
      if k > len(nums):
          k = len(nums)

      # Add condition for small size
      if len(nums) <= k:
          if len(set(nums)) < k:
              return True
          else:
              return False

      # # Use set and sliding window
      # for i in range(len(nums) - k):
      #     if len(set(nums[i:i+k+1])) <= k:
      #         return True
      # return False

      # Use dictionary O(n)
      d : Dict(int, int) = {}
      for i, numi in enumerate(nums):
          if d.get(numi, None) is not None:
              if 0 < abs(d[numi] - i) <= k:
                  return True
          d[numi] = i
      return False
