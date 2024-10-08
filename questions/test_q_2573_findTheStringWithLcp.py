import pytest
from q_2573_findTheStringWithLcp import Solution


@pytest.mark.parametrize(
    "lcp, output",
    [
        ([[4, 0, 2, 0], [0, 3, 0, 1], [2, 0, 2, 0], [0, 1, 0, 1]], "abab"),
        ([[4, 3, 2, 1], [3, 3, 2, 1], [2, 2, 2, 1], [1, 1, 1, 1]], "aaaa"),
        ([[4, 3, 2, 1], [3, 3, 2, 1], [2, 2, 2, 1], [1, 1, 1, 3]], ""),
    ],
)
class TestSolution:
    def test_findTheString(self, lcp: List[List[int]], output: str):
        sc = Solution()
        assert (
            sc.findTheString(
                lcp,
            )
            == output
        )
