import pytest
from q_1529_minimumSuffixFlips import Solution


@pytest.mark.parametrize("target, output", [("10111", 3), ("101", 3), ("00000", 0)])
class TestSolution:
    def test_minFlips(self, target: str, output: int):
        sc = Solution()
        assert (
            sc.minFlips(
                target,
            )
            == output
        )
