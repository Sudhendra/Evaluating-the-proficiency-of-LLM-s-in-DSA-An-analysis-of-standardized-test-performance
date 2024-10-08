import pytest
from q_2029_stoneGameIx import Solution


@pytest.mark.parametrize(
    "stones, output", [([2, 1], True), ([2], False), ([5, 1, 2, 4, 3], False)]
)
class TestSolution:
    def test_stoneGameIX(self, stones: List[int], output: bool):
        sc = Solution()
        assert (
            sc.stoneGameIX(
                stones,
            )
            == output
        )
