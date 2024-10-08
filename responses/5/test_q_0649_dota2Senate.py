import pytest
from q_0649_dota2Senate import Solution


@pytest.mark.parametrize("senate, output", [("RD", "Radiant"), ("RDD", "Dire")])
class TestSolution:
    def test_predictPartyVictory(self, senate: str, output: str):
        sc = Solution()
        assert (
            sc.predictPartyVictory(
                senate,
            )
            == output
        )
