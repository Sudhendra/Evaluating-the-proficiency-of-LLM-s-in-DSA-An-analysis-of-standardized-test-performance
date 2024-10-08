import pytest
from q_2211_countCollisionsOnARoad import Solution


@pytest.mark.parametrize("directions, output", [("RLRSLL", 5), ("LLRR", 0)])
class TestSolution:
    def test_countCollisions(self, directions: str, output: int):
        sc = Solution()
        assert (
            sc.countCollisions(
                directions,
            )
            == output
        )
