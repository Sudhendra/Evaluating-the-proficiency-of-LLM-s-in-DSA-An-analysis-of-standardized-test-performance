import pytest
from q_2086_minimumNumberOfFoodBucketsToFeedTheHamsters import Solution


@pytest.mark.parametrize("hamsters, output", [("H..H", 2), (".H.H.", 1), (".HHH.", -1)])
class TestSolution:
    def test_minimumBuckets(self, hamsters: str, output: int):
        sc = Solution()
        assert (
            sc.minimumBuckets(
                hamsters,
            )
            == output
        )
