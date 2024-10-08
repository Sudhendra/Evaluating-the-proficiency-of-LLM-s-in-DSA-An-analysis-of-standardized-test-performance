import pytest
from q_0546_removeBoxes import Solution


@pytest.mark.parametrize(
    "boxes, output", [([1, 3, 2, 2, 2, 3, 4, 3, 1], 23), ([1, 1, 1], 9), ([1], 1)]
)
class TestSolution:
    def test_removeBoxes(self, boxes: List[int], output: int):
        sc = Solution()
        assert (
            sc.removeBoxes(
                boxes,
            )
            == output
        )
