import pytest
from q_1394_findLuckyIntegerInAnArray import Solution


@pytest.mark.parametrize(
    "arr, output", [([2, 2, 3, 4], 2), ([1, 2, 2, 3, 3, 3], 3), ([2, 2, 2, 3, 3], -1)]
)
class TestSolution:
    def test_findLucky(self, arr: List[int], output: int):
        sc = Solution()
        assert (
            sc.findLucky(
                arr,
            )
            == output
        )
