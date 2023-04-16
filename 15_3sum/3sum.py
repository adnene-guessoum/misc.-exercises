"""
https://leetcode.com/problems/3sum/

Given an integer array nums,
return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resultat = []

        # ranger liste pour recherche double pointer (O(nlogn))
        nums.sort()

        # premieres valeurs de somme (O(n))
        for i, num in enumerate(nums):

            # doublons dans nums conduisent aux mêmes triplets res 
            # liste rangée, donc si num == nums[i-1], alors on passe
            if i > 0 and num == nums[i-1]:
                continue

            # ensuite, solution "two sum" avec pointer droite et gauche
            droite = len(nums) - 1
            gauche = i + 1 # laisse de côté le num courant (premier du triplet)

            # tant que les pointeurs ne se sont pas croisés (O(n))
            while gauche < droite:

                three_sum = num + nums[gauche] + nums[droite]

                if three_sum == 0:
                    resultat.append([num, nums[gauche], nums[droite]])
                    # eviter d'evaluer les mêmes triplets
                    # si les valeurs sont les mêmes, on passe
                    gauche += 1
                    while gauche < droite and nums[gauche] == nums[gauche - 1]:
                        gauche += 1

                elif three_sum < 0:
                    gauche += 1

                else:
                    droite -= 1

        # solution generale en O(n^2) donc (O(n^2) + O(nlogn)
        return resultat
