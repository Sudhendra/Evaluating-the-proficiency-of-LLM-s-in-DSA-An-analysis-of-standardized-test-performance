import pytest
from q_2938_separateBlackAndWhiteBalls import Solution


@pytest.mark.parametrize("s, output", [("101", 1), ("100", 2), ("0111", 0)])
class TestSolution:
    def test_minimumSteps(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.minimumSteps(
                s,
            )
            == output
        )
