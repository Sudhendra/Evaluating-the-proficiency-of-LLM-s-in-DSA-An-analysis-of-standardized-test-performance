import pytest
from q_1690_stoneGameVii import Solution


@pytest.mark.parametrize(
    "stones, output", [([5, 3, 1, 4, 2], 6), ([7, 90, 5, 1, 100, 10, 10, 2], 122)]
)
class TestSolution:
    def test_stoneGameVII(self, stones: List[int], output: int):
        sc = Solution()
        assert (
            sc.stoneGameVII(
                stones,
            )
            == output
        )
