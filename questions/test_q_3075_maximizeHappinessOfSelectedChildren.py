import pytest
from q_3075_maximizeHappinessOfSelectedChildren import Solution


@pytest.mark.parametrize(
    "happiness, k, output",
    [([1, 2, 3], 2, 4), ([1, 1, 1, 1], 2, 1), ([2, 3, 4, 5], 1, 5)],
)
class TestSolution:
    def test_maximumHappinessSum(self, happiness: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.maximumHappinessSum(
                happiness,
                k,
            )
            == output
        )
