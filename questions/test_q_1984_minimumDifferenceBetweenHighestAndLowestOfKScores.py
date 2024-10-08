import pytest
from q_1984_minimumDifferenceBetweenHighestAndLowestOfKScores import Solution


@pytest.mark.parametrize("nums, k, output", [([90], 1, 0), ([9, 4, 1, 7], 2, 2)])
class TestSolution:
    def test_minimumDifference(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.minimumDifference(
                nums,
                k,
            )
            == output
        )
