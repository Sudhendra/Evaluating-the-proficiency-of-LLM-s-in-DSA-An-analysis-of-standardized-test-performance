import pytest
from q_1953_maximumNumberOfWeeksForWhichYouCanWork import Solution


@pytest.mark.parametrize("milestones, output", [([1, 2, 3], 6), ([5, 2, 1], 7)])
class TestSolution:
    def test_numberOfWeeks(self, milestones: List[int], output: int):
        sc = Solution()
        assert (
            sc.numberOfWeeks(
                milestones,
            )
            == output
        )
