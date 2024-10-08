import pytest
from q_1927_sumGame import Solution


@pytest.mark.parametrize(
    "num, output", [("5023", False), ("25??", True), ("?3295???", False)]
)
class TestSolution:
    def test_sumGame(self, num: str, output: bool):
        sc = Solution()
        assert (
            sc.sumGame(
                num,
            )
            == output
        )
