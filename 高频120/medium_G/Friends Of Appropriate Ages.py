class Solution:
    """
    @param ages:
    @return: nothing
    @## APPROACH : COUNTER ##
    """

    def numFriendRequests(self, ages):

        ages = collections.Counter(ages)

        count = 0

        for ageA, countA in ages.items():
            for ageB, countB in ages.items():
                if ageA * 0.5 + 7 >= ageB:
                    continue
                if ageA < ageB:
                    continue

                count += countA * countB
                # ?
                if ageA == ageB:
                    count -= countA
        return count
