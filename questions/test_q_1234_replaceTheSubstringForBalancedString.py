import pytest
from q_1234_replaceTheSubstringForBalancedString import Solution


@pytest.mark.parametrize("s, output", [("QWER", 0), ("QQWE", 1), ("QQQW", 2)])
class TestSolution:
    def test_balancedString(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.balancedString(
                s,
            )
            == output
        )
