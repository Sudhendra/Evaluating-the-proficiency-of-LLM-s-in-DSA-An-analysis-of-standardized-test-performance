import pytest
from q_2217_findPalindromeWithFixedLength import Solution


@pytest.mark.parametrize(
    "queries, intLength, output",
    [
        ([1, 2, 3, 4, 5, 90], 3, [101, 111, 121, 131, 141, 999]),
        ([2, 4, 6], 4, [1111, 1331, 1551]),
    ],
)
class TestSolution:
    def test_kthPalindrome(self, queries: List[int], intLength: int, output: List[int]):
        sc = Solution()
        assert (
            sc.kthPalindrome(
                queries,
                intLength,
            )
            == output
        )
