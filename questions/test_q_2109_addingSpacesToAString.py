import pytest
from q_2109_addingSpacesToAString import Solution


@pytest.mark.parametrize(
    "s, spaces, output",
    [
        ("LeetcodeHelpsMeLearn", [8, 13, 15], "Leetcode Helps Me Learn"),
        ("icodeinpython", [1, 5, 7, 9], "i code in py thon"),
        ("spacing", [0, 1, 2, 3, 4, 5, 6], " s p a c i n g"),
    ],
)
class TestSolution:
    def test_addSpaces(self, s: str, spaces: List[int], output: str):
        sc = Solution()
        assert (
            sc.addSpaces(
                s,
                spaces,
            )
            == output
        )
