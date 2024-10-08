import pytest
from q_1936_addMinimumNumberOfRungs import Solution


@pytest.mark.parametrize(
    "rungs, dist, output",
    [([1, 3, 5, 10], 2, 2), ([3, 6, 8, 10], 3, 0), ([3, 4, 6, 7], 2, 1)],
)
class TestSolution:
    def test_addRungs(self, rungs: List[int], dist: int, output: int):
        sc = Solution()
        assert (
            sc.addRungs(
                rungs,
                dist,
            )
            == output
        )
