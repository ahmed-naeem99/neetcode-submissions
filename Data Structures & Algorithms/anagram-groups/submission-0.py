class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {}

        for s in strs:
            sorted_key = "".join(sorted(s))

            if sorted_key not in res:
                res[sorted_key] = []
            
            res[sorted_key].append(s)

        return list(res.values())