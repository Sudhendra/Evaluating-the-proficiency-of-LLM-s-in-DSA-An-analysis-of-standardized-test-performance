import pytest
from q_0042_trappingRainWater import Solution


@pytest.mark.parametrize(
    "height, output",
    [([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6), ([4, 2, 0, 3, 2, 5], 9)],
)
class TestSolution:
    def test_trap(self, height: List[int], output: int):
        sc = Solution()
        assert (
            sc.trap(
                height,
            )
            == output
        )
