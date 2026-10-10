class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = {}

        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1

        freq_buckets = [[] for i in range(len(nums) + 1)]

        for num, count in frequencies.items():
            freq_buckets[count].append(num)

        res = []

        for i in range(len(freq_buckets) - 1, 0, -1):
            for num in freq_buckets[i]:
                res.append(num)

                if len(res) == k:
                    return res


        return res