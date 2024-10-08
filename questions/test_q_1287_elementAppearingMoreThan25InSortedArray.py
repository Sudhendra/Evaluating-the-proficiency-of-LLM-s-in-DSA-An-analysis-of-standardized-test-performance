import pytest
from q_1287_elementAppearingMoreThan25InSortedArray import Solution


@pytest.mark.parametrize(
    "arr, output", [([1, 2, 2, 6, 6, 6, 6, 7, 10], 6), ([1, 1], 1)]
)
class TestSolution:
    def test_findSpecialInteger(self, arr: List[int], output: int):
        sc = Solution()
        assert (
            sc.findSpecialInteger(
                arr,
            )
            == output
        )
