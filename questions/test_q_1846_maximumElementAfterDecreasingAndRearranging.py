import pytest
from q_1846_maximumElementAfterDecreasingAndRearranging import Solution


@pytest.mark.parametrize(
    "arr, output", [([2, 2, 1, 2, 1], 2), ([100, 1, 1000], 3), ([1, 2, 3, 4, 5], 5)]
)
class TestSolution:
    def test_maximumElementAfterDecrementingAndRearranging(
        self, arr: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.maximumElementAfterDecrementingAndRearranging(
                arr,
            )
            == output
        )
