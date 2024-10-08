import pytest
from q_1944_numberOfVisiblePeopleInAQueue import Solution


@pytest.mark.parametrize(
    "heights, output",
    [([10, 6, 8, 5, 11, 9], [3, 1, 2, 1, 1, 0]), ([5, 1, 2, 3, 10], [4, 1, 1, 1, 0])],
)
class TestSolution:
    def test_canSeePersonsCount(self, heights: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.canSeePersonsCount(
                heights,
            )
            == output
        )
