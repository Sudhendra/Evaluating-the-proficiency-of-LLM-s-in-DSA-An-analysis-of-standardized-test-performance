import pytest
from q_1124_longestWellPerformingInterval import Solution


@pytest.mark.parametrize("hours, output", [([9, 9, 6, 0, 6, 6, 9], 3), ([6, 6, 6], 0)])
class TestSolution:
    def test_longestWPI(self, hours: List[int], output: int):
        sc = Solution()
        assert (
            sc.longestWPI(
                hours,
            )
            == output
        )
