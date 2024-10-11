from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        # diff btw normal dict and default is that we can create keys which don't exist
        # it creates those default keys by the type we call - list - in this case

        for val in strs:
            # the key is sorted letters in a word 
            # for 'ate' its ['a','e','t'] as key
            key = str(sorted(val))
            # value is the combined word itself which has those letters
            # since this is defaultdict, its easy to create new keys and add values
            ans[key].append(val)

        return ans.values()
