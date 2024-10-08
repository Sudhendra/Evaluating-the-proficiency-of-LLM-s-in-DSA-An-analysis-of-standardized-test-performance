import pytest
from q_0873_lengthOfLongestFibonacciSubsequence import Solution


@pytest.mark.parametrize(
    "arr, output", [([1, 2, 3, 4, 5, 6, 7, 8], 5), ([1, 3, 7, 11, 12, 14, 18], 3)]
)
class TestSolution:
    def test_lenLongestFibSubseq(self, arr: List[int], output: int):
        sc = Solution()
        assert (
            sc.lenLongestFibSubseq(
                arr,
            )
            == output
        )
