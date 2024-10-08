import pytest
from q_0781_rabbitsInForest import Solution


@pytest.mark.parametrize("answers, output", [([1, 1, 2], 5), ([10, 10, 10], 11)])
class TestSolution:
    def test_numRabbits(self, answers: List[int], output: int):
        sc = Solution()
        assert (
            sc.numRabbits(
                answers,
            )
            == output
        )
