import pytest
from q_1014_bestSightseeingPair import Solution


@pytest.mark.parametrize("values, output", [([8, 1, 5, 2, 6], 11), ([1, 2], 2)])
class TestSolution:
    def test_maxScoreSightseeingPair(self, values: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxScoreSightseeingPair(
                values,
            )
            == output
        )
