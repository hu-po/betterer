class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if not nums or len(nums) < 3:
            return []
        
        # Brute force
        # answer: Set[List[int]] = []
        # for p in itertools.combinations([_ for _ in range(len(nums))], 3):
        #     if nums[p[0]] + nums[p[1]] + nums[p[2]] == 0:
        #         triplet: List[int] = sorted([nums[p[0]], nums[p[1]], nums[p[2]]])
        #         if not triplet in answer:
        #             answer.append(triplet)
        # return list(answer)
    
        # if we fix the first number, this becomes two sum
        answer: Set[List[int]] = []
        
        # O(nlogn) sort
        nums = sorted(nums)
        
        # O(n**2)
        for p1 in range(len(nums) - 2):
            # two pointer solution
            for p2 in range(p1+1, len(nums) - 1):
                p3: int = len(nums) - 1
                while nums[p1] + nums[p2] + nums[p3] >= 0 and p3 > p2:
                    if nums[p1] + nums[p2] + nums[p3] == 0:
                        triplet = sorted([nums[p1], nums[p2], nums[p3]])
                        if not triplet in answer:
                            answer.append(sorted([nums[p1], nums[p2], nums[p3]]))
                    p3 -= 1
                    
        return list(answer)
