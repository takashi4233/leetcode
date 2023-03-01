import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        (["i", "love", "leetcode", "i", "love", "coding"], 2, ["i", "love"]),
        (
            ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
            4,
            ["the", "is", "sunny", "day"],
        ),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.topKFrequent(s, t) == expected
