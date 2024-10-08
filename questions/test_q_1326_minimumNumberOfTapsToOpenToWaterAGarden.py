import pytest
from q_1326_minimumNumberOfTapsToOpenToWaterAGarden import Solution


@pytest.mark.parametrize(
    "n, ranges, output", [(5, [3, 4, 1, 1, 0, 0], 1), (3, [0, 0, 0, 0], -1)]
)
class TestSolution:
    def test_minTaps(self, n: int, ranges: List[int], output: int):
        sc = Solution()
        assert (
            sc.minTaps(
                n,
                ranges,
            )
            == output
        )
