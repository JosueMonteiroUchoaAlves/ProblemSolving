#https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicionario = {}
        for item in strs:
            i= ''.join(sorted(item))
            if i not in dicionario:
                dicionario[i] = [item]
            elif i in dicionario:
                dicionario[i].append(item)
            
        return [dicionario[item] for item in dicionario]
