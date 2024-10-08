import pytest
from q_0874_walkingRobotSimulation import Solution


@pytest.mark.parametrize(
    "commands, obstacles, output",
    [([4, -1, 3], [], 25), ([4, -1, 4, -2, 4], [[2, 4]], 65), ([6, -1, -1, 6], [], 36)],
)
class TestSolution:
    def test_robotSim(
        self, commands: List[int], obstacles: List[List[int]], output: int
    ):
        sc = Solution()
        assert (
            sc.robotSim(
                commands,
                obstacles,
            )
            == output
        )
