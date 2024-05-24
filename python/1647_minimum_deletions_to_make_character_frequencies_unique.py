class Solution:
    def minDeletions(self, s: str) -> int:
        counts = collections.Counter(s)

        used = set()
        deletions = 0

        for count in counts.values():
            while count > 0 and count in used:
                count -= 1
                deletions += 1

            used.add(count)

        return deletions
