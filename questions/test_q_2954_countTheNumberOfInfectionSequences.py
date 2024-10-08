import pytest
from q_2954_countTheNumberOfInfectionSequences import Solution


@pytest.mark.parametrize("n, sick, output", [(5, [0, 4], 4), (4, [1], 3)])
class TestSolution:
    def test_numberOfSequence(self, n: int, sick: List[int], output: int):
        sc = Solution()
        assert (
            sc.numberOfSequence(
                n,
                sick,
            )
            == output
        )
