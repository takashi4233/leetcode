from typing import List
from typing import Optional


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
        second = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
        third = ["z", "x", "c", "v", "b", "n", "m"]
        ans = []

        for word in words:
            word_lower = word.lower()
            # print(f"{word}")
            dict = {"f": 0, "s": 0, "t": 0}
            for w in word_lower:
                if w in first:
                    dict["f"] = dict["f"] + 1
                if w in second:
                    dict["s"] = dict["s"] + 1
                if w in third:
                    dict["t"] = dict["t"] + 1
            for value in dict.values():
                # print(f"{value}")
                if value == len(word):
                    ans.append(word)
        return ans

        # for word in words:
        #     word_lower = word.lower()
        #     if word_lower[0] in first:
        #         print(f"{word_lower[0]} in first")
        #         for w in word_lower:
        #             print(f"{w}")
        #             if w not in first:
        #                 print(f"{w} not in first")
        #                 break
        #         ans.append(word)
        #     if word_lower[0] in second:
        #         print(f"{word_lower[0]} in second")
        #         for w in word_lower:
        #             if w not in second:
        #                 print(f"{w} not in second")
        #                 break
        #         ans.append(word)
        #     if word_lower[0] in third:
        #         print(f"{word_lower[0]} in third")
        #         for w in word_lower:
        #             if w not in third:
        #                 print(f"{w} not in third")
        #                 break
        #         ans.append(word)
        return ans

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    words = ["Hello", "Alaska", "Dad", "Peace"]
    output = ["Alaska", "Dad"]
    sol.test(sol.findWords(words), output)


if __name__ == "__main__":
    main()
