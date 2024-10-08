front_matter = {
    "qid": 229,
    "title": "Majority Element II",
    "titleSlug": "majority-element-ii",
    "difficulty": "Medium",
    "tags": ["Array", "Hash Table", "Sorting", "Counting"],
}

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        if not nums:
            return res
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        if count1 > len(nums)/3:
            res.append(candidate1)
        if count2 > len(nums)/3:
            res.append(candidate2)

        return res