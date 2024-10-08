import pytest
from q_0335_selfCrossing import Solution


@pytest.mark.parametrize(
    "distance, output",
    [([2, 1, 1, 2], True), ([1, 2, 3, 4], False), ([1, 1, 1, 2, 1], True)],
)
class TestSolution:
    def test_isSelfCrossing(self, distance: List[int], output: bool):
        sc = Solution()
        assert (
            sc.isSelfCrossing(
                distance,
            )
            == output
        )
