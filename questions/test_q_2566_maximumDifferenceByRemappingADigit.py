import pytest
from q_2566_maximumDifferenceByRemappingADigit import Solution


@pytest.mark.parametrize("num, output", [(11891, 99009), (90, 99)])
class TestSolution:
    def test_minMaxDifference(self, num: int, output: int):
        sc = Solution()
        assert (
            sc.minMaxDifference(
                num,
            )
            == output
        )
