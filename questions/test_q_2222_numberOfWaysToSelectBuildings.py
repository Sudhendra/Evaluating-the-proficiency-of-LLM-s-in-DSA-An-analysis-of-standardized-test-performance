import pytest
from q_2222_numberOfWaysToSelectBuildings import Solution


@pytest.mark.parametrize("s, output", [("001101", 6), ("11100", 0)])
class TestSolution:
    def test_numberOfWays(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.numberOfWays(
                s,
            )
            == output
        )
