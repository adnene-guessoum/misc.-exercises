''' https://leetcode.com/problems/permutations/

Given an array of distinct integers, return all possible permutations.
you can return the answer in any order.
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        resultat = []

        # approche recursive: définir Cas de base
        if len(nums) == 1:
            return [nums.copy()]

        for i in range(len(nums)):
            # reduction du pblme
            n = nums.pop(0)

            # appel recursif
            permutations = self.permute(nums)

            # reintroduction de valeur pop dans les listes permutées (fin)
            for permutation in permutations:
                permutation.append(n)

            # ajout des nouvelles permutations à la liste de resultats
            resultat.extend(permutations)

            # restauration de la liste originale (nums) pour prochaine rec 
            nums.append(n)

        return resultat


        

