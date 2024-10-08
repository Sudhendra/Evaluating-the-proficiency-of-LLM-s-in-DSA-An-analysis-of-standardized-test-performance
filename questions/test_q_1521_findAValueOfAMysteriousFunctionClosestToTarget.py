import pytest
from q_1521_findAValueOfAMysteriousFunctionClosestToTarget import Solution


@pytest.mark.parametrize(
    "arr, target, output",
    [
        ([9, 12, 3, 7, 15], 5, 2),
        ([1000000, 1000000, 1000000], 1, 999999),
        ([1, 2, 4, 8, 16], 0, 0),
    ],
)
class TestSolution:
    def test_closestToTarget(self, arr: List[int], target: int, output: int):
        sc = Solution()
        assert (
            sc.closestToTarget(
                arr,
                target,
            )
            == output
        )
