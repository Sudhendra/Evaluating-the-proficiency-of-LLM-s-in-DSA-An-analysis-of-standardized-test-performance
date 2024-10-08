import pytest
from q_1013_partitionArrayIntoThreePartsWithEqualSum import Solution


@pytest.mark.parametrize(
    "arr, output",
    [
        ([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1], True),
        ([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1], False),
        ([3, 3, 6, 5, -2, 2, 5, 1, -9, 4], True),
    ],
)
class TestSolution:
    def test_canThreePartsEqualSum(self, arr: List[int], output: bool):
        sc = Solution()
        assert (
            sc.canThreePartsEqualSum(
                arr,
            )
            == output
        )
