import pytest
from q_1732_findTheHighestAltitude import Solution


@pytest.mark.parametrize(
    "gain, output", [([-5, 1, 5, 0, -7], 1), ([-4, -3, -2, -1, 4, 3, 2], 0)]
)
class TestSolution:
    def test_largestAltitude(self, gain: List[int], output: int):
        sc = Solution()
        assert (
            sc.largestAltitude(
                gain,
            )
            == output
        )
