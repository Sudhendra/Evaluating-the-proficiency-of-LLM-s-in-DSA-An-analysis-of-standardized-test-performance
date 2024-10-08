import pytest
from q_2274_maximumConsecutiveFloorsWithoutSpecialFloors import Solution


@pytest.mark.parametrize(
    "bottom, top, special, output", [(2, 9, [4, 6], 3), (6, 8, [7, 6, 8], 0)]
)
class TestSolution:
    def test_maxConsecutive(
        self, bottom: int, top: int, special: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.maxConsecutive(
                bottom,
                top,
                special,
            )
            == output
        )
