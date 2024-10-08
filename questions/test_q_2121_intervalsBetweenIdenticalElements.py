import pytest
from q_2121_intervalsBetweenIdenticalElements import Solution


@pytest.mark.parametrize(
    "arr, output",
    [([2, 1, 3, 1, 2, 3, 3], [4, 2, 7, 2, 4, 4, 5]), ([10, 5, 10, 10], [5, 0, 3, 4])],
)
class TestSolution:
    def test_getDistances(self, arr: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.getDistances(
                arr,
            )
            == output
        )
