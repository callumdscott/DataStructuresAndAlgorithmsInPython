class PatternMatching:
    """Pattern Matcher for storing a target string and a pattern to match it to."""

    def __init__(self, target, pattern):
        """Initialises a PatternMatcher class, initialising the target string and the pattern string."""
        self.target = target
        self.pattern = pattern

    def karp_rabin(self):
        """Karp-Rabin Pattern Matching Algorithm, using hashing to compare substrings for equality"""
        if len(self.pattern) == 0:
            return 0
        if len(self.pattern) < len(self.target):
            hash_key = hash(self.pattern)
            for i in range(len(self.target) - len(self.pattern) + 1):
                target_substring = self.target[i: i + len(self.pattern)]
                hash_try = hash(target_substring)
                if hash_try == hash_key:
                    if self.test_string_equality(self.pattern, target_substring):
                        return i
        return -1

    @staticmethod
    def test_string_equality(string_1, string_2):
        """Iterative comparison to avoid misidentifying matches with colliding hash values."""
        assert len(string_1) == len(string_2)
        for i in range(len(string_1)):
            if string_1[i] != string_2[i]:
                return False
        return True

    def find_kmp(self):
        """Knuth Morris Pratt algorithm for pattern matching using a failure function to calculate max shift required
        before continuing search."""
        n, m = len(self.target), len(self.pattern)
        if m == 0:
            return 0
        fail = self.compute_kmp_fail()
        j, k = 0, 0
        while j < n:
            if self.target[j] == self.pattern[k]:
                if k == m - 1:
                    return j - m + 1
                j += 1
                k += 1
            elif k > 0:
                k = fail[k - 1]
            else:
                j += 1
        return -1

    def compute_kmp_fail(self):
        """Computes a failure function array, for shift size upon failure by precomputing reoccurring sub-sequences."""
        m = len(self.pattern)
        fail = [0] * m
        j = 1
        k = 0
        while j < m:
            if self.pattern[j] == self.pattern[k]:
                fail[j] = k + 1
                j += 1
                k += 1
            elif k > 0:
                k = fail[k - 1]
            else:
                j += 1
        return fail
