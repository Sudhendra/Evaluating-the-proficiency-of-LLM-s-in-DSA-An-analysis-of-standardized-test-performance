import pytest
from q_1202_smallestStringWithSwaps import Solution


@pytest.mark.parametrize(
    "s, pairs, output",
    [
        ("dcab", [[0, 3], [1, 2]], "bacd"),
        ("dcab", [[0, 3], [1, 2], [0, 2]], "abcd"),
        ("cba", [[0, 1], [1, 2]], "abc"),
    ],
)
class TestSolution:
    def test_smallestStringWithSwaps(self, s: str, pairs: List[List[int]], output: str):
        sc = Solution()
        assert (
            sc.smallestStringWithSwaps(
                s,
                pairs,
            )
            == output
        )
