from collections import Counter

    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        total = 0

        for k, c in count.items():
            group_size = k + 1
            groups = (c + k) // group_size  # Ceiling of (c / group_size)
            total += groups * group_size

        return total
