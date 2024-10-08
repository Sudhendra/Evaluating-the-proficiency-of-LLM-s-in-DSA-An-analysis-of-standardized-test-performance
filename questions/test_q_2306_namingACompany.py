import pytest
from q_2306_namingACompany import Solution


@pytest.mark.parametrize(
    "ideas, output",
    [(["coffee", "donuts", "time", "toffee"], 6), (["lack", "back"], 0)],
)
class TestSolution:
    def test_distinctNames(self, ideas: List[str], output: int):
        sc = Solution()
        assert (
            sc.distinctNames(
                ideas,
            )
            == output
        )
