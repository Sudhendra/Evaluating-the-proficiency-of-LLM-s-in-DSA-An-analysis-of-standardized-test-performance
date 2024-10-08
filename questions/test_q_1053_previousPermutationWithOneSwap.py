import pytest
from q_1053_previousPermutationWithOneSwap import Solution


@pytest.mark.parametrize(
    "arr, output",
    [
        ([3, 2, 1], [3, 1, 2]),
        ([1, 1, 5], [1, 1, 5]),
        ([1, 9, 4, 6, 7], [1, 7, 4, 6, 9]),
    ],
)
class TestSolution:
    def test_prevPermOpt1(self, arr: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.prevPermOpt1(
                arr,
            )
            == output
        )
