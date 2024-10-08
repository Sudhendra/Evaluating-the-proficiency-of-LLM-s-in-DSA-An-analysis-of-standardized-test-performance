import pytest
from q_0403_frogJump import Solution


@pytest.mark.parametrize(
    "stones, output",
    [([0, 1, 3, 5, 6, 8, 12, 17], True), ([0, 1, 2, 3, 4, 8, 9, 11], False)],
)
class TestSolution:
    def test_canCross(self, stones: List[int], output: bool):
        sc = Solution()
        assert (
            sc.canCross(
                stones,
            )
            == output
        )
