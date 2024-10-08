import pytest
from q_2751_robotCollisions import Solution


@pytest.mark.parametrize(
    "positions, healths, directions, output",
    [
        ([5, 4, 3, 2, 1], [2, 17, 9, 15, 10], "RRRRR", [2, 17, 9, 15, 10]),
        ([3, 5, 2, 6], [10, 10, 15, 12], "RLRL", [14]),
        ([1, 2, 5, 6], [10, 10, 11, 11], "RLRL", []),
    ],
)
class TestSolution:
    def test_survivedRobotsHealths(
        self,
        positions: List[int],
        healths: List[int],
        directions: str,
        output: List[int],
    ):
        sc = Solution()
        assert (
            sc.survivedRobotsHealths(
                positions,
                healths,
                directions,
            )
            == output
        )
