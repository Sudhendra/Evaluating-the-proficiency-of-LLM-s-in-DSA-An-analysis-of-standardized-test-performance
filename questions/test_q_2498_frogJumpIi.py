import pytest
from q_2498_frogJumpIi import Solution


@pytest.mark.parametrize("stones, output", [([0, 2, 5, 6, 7], 5), ([0, 3, 9], 9)])
class TestSolution:
    def test_maxJump(self, stones: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxJump(
                stones,
            )
            == output
        )
