import pytest
from q_1872_stoneGameViii import Solution


@pytest.mark.parametrize(
    "stones, output",
    [([-1, 2, -3, 4, -5], 5), ([7, -6, 5, 10, 5, -2, -6], 13), ([-10, -12], -22)],
)
class TestSolution:
    def test_stoneGameVIII(self, stones: List[int], output: int):
        sc = Solution()
        assert (
            sc.stoneGameVIII(
                stones,
            )
            == output
        )
