class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):

        self.persons = persons
        self.times = times
        self. cnt = defaultdict(int)
        self. leading = []
        self.maximum = 0

        for i,j in enumerate(self.times):

            self.cnt[self.persons[i]] += 1

            if not self.leading:

                self.leading.append(self.persons[i])
                self.maximum = 1

            elif self.cnt[self.persons[i]] >= self.maximum :

                self.leading.append(self.persons[i])
                self.maximum = self.cnt[persons[i]]

            else:

                self.leading.append(self.leading[-1])


    def q(self, t: int) -> int:

        l = 0 
        r = len(self.times) - 1

        while l <= r :

            mid = l + (r - l) // 2

            if self.times [mid] < t :

                l = mid + 1

            elif self.times [mid] > t :

                r = mid - 1

            else:

                return self.leading[mid]

        return self.leading[r]




        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
