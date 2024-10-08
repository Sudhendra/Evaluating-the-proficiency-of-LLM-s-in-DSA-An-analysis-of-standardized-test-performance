import pytest
from q_0845_longestMountainInArray import Solution


@pytest.mark.parametrize("arr, output", [([2, 1, 4, 7, 3, 2, 5], 5), ([2, 2, 2], 0)])
class TestSolution:
    def test_longestMountain(self, arr: List[int], output: int):
        sc = Solution()
        assert (
            sc.longestMountain(
                arr,
            )
            == output
        )
