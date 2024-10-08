import pytest
from q_1385_findTheDistanceValueBetweenTwoArrays import Solution


@pytest.mark.parametrize(
    "arr1, arr2, d, output",
    [
        ([4, 5, 8], [10, 9, 1, 8], 2, 2),
        ([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3, 2),
        ([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6, 1),
    ],
)
class TestSolution:
    def test_findTheDistanceValue(
        self, arr1: List[int], arr2: List[int], d: int, output: int
    ):
        sc = Solution()
        assert (
            sc.findTheDistanceValue(
                arr1,
                arr2,
                d,
            )
            == output
        )
