import pytest
from q_2707_extraCharactersInAString import Solution


@pytest.mark.parametrize(
    "s, dictionary, output",
    [
        ("leetscode", ["leet", "code", "leetcode"], 1),
        ("sayhelloworld", ["hello", "world"], 3),
    ],
)
class TestSolution:
    def test_minExtraChar(self, s: str, dictionary: List[str], output: int):
        sc = Solution()
        assert (
            sc.minExtraChar(
                s,
                dictionary,
            )
            == output
        )
