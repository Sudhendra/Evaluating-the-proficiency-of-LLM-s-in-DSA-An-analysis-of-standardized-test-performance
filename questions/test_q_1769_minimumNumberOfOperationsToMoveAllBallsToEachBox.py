import pytest
from q_1769_minimumNumberOfOperationsToMoveAllBallsToEachBox import Solution


@pytest.mark.parametrize(
    "boxes, output", [("110", [1, 1, 3]), ("001011", [11, 8, 5, 4, 3, 4])]
)
class TestSolution:
    def test_minOperations(self, boxes: str, output: List[int]):
        sc = Solution()
        assert (
            sc.minOperations(
                boxes,
            )
            == output
        )
