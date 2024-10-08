import pytest
from q_1687_deliveringBoxesFromStorageToPorts import Solution


@pytest.mark.parametrize(
    "boxes, portsCount, maxBoxes, maxWeight, output",
    [
        ([[1, 1], [2, 1], [1, 1]], 2, 3, 3, 4),
        ([[1, 2], [3, 3], [3, 1], [3, 1], [2, 4]], 3, 3, 6, 6),
        ([[1, 4], [1, 2], [2, 1], [2, 1], [3, 2], [3, 4]], 3, 6, 7, 6),
    ],
)
class TestSolution:
    def test_boxDelivering(
        self,
        boxes: List[List[int]],
        portsCount: int,
        maxBoxes: int,
        maxWeight: int,
        output: int,
    ):
        sc = Solution()
        assert (
            sc.boxDelivering(
                boxes,
                portsCount,
                maxBoxes,
                maxWeight,
            )
            == output
        )
