from typing import List
from typing import Optional


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def helper(res, path, options):
            if len(options) == 0:
                res.append(path)
            else:
                # Take one element from string and update remaining options
                c = options[0]
                options = options[1:]

                # If the element is number, simply append it and continue
                # otherwise append both the upper and lower case of the letter
                if c.isdigit():
                    helper(res, path + c, options)
                else:
                    helper(res, path + c.lower(), options)
                    helper(res, path + c.upper(), options)

        helper(res, "", s)
        return res

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = "a1b2"
    output = ["a1b2", "a1B2", "A1b2", "A1B2"]
    sol.test(sol.letterCasePermutation(input), output)


if __name__ == "__main__":
    main()
