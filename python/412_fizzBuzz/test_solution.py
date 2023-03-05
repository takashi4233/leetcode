import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        (3, "", ["1", "2", "Fizz"]),
        (5, "", ["1", "2", "Fizz", "4", "Buzz"]),
        (
            15,
            "",
            [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz",
            ],
        ),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.fizzBuzz(s) == expected
