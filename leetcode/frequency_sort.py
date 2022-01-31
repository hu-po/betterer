class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count: Dict[int, int] = collections.Counter(nums)
        return sorted(nums, key= lambda num: (count[num], -num))
