import pytest
from q_1191_kConcatenationMaximumSum import Solution


@pytest.mark.parametrize(
    "arr, k, output", [([1, 2], 3, 9), ([1, -2, 1], 5, 2), ([-1, -2], 7, 0)]
)
class TestSolution:
    def test_kConcatenationMaxSum(self, arr: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.kConcatenationMaxSum(
                arr,
                k,
            )
            == output
        )
