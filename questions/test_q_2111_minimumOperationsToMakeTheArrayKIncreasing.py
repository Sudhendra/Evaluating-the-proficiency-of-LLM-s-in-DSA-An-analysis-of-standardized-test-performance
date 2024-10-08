import pytest
from q_2111_minimumOperationsToMakeTheArrayKIncreasing import Solution


@pytest.mark.parametrize(
    "arr, k, output",
    [([5, 4, 3, 2, 1], 1, 4), ([4, 1, 5, 2, 6, 2], 2, 0), ([4, 1, 5, 2, 6, 2], 3, 2)],
)
class TestSolution:
    def test_kIncreasing(self, arr: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.kIncreasing(
                arr,
                k,
            )
            == output
        )
