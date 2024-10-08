import pytest
from q_1374_generateAStringWithCharactersThatHaveOddCounts import Solution


@pytest.mark.parametrize("n, output", [(4, "pppz"), (2, "xy"), (7, "holasss")])
class TestSolution:
    def test_generateTheString(self, n: int, output: str):
        sc = Solution()
        assert (
            sc.generateTheString(
                n,
            )
            == output
        )
