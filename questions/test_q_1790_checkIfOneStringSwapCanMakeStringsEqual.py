import pytest
from q_1790_checkIfOneStringSwapCanMakeStringsEqual import Solution


@pytest.mark.parametrize(
    "s1, s2, output",
    [("bank", "kanb", True), ("attack", "defend", False), ("kelb", "kelb", True)],
)
class TestSolution:
    def test_areAlmostEqual(self, s1: str, s2: str, output: bool):
        sc = Solution()
        assert (
            sc.areAlmostEqual(
                s1,
                s2,
            )
            == output
        )
