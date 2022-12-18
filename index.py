class Solution:
    def __init__(self):
        self.solve()

    def number_of_subsequences(self, text: str, sentence: str) -> int:
        """
        Return the number of subsequences in a text given a sentence

        Time complexity: O(mn)
        """
        m = len(text)
        n = len(sentence)

        dp_table = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(n + 1):
            dp_table[0][i] = 0

        for i in range(m + 1):
            dp_table[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if text[i - 1] == sentence[j - 1]:
                    dp_table[i][j] = dp_table[i - 1][j - 1] + dp_table[i - 1][j]
                else:
                    dp_table[i][j] = dp_table[i - 1][j]

        return dp_table[m][n]

    def solve(self):
        """
        Handles user input
        """
        p = int(input())

        while p > 0:
            s = input()
            t = input()
            n = self.number_of_subsequences(text=t, sentence=s)
            print(n)
            p -= 1


Solution()
