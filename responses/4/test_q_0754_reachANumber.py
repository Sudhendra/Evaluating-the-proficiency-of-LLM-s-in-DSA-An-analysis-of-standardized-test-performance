import pytest
from q_0754_reachANumber import Solution


@pytest.mark.parametrize("target, output", [(2, 3), (3, 2)])
class TestSolution:
    def test_reachNumber(self, target: int, output: int):
        sc = Solution()
        assert (
            sc.reachNumber(
                target,
            )
            == output
        )
