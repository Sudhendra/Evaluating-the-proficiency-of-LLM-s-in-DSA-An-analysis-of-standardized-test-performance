import pytest
from q_1320_minimumDistanceToTypeAWordUsingTwoFingers import Solution


@pytest.mark.parametrize("word, output", [("CAKE", 3), ("HAPPY", 6)])
class TestSolution:
    def test_minimumDistance(self, word: str, output: int):
        sc = Solution()
        assert (
            sc.minimumDistance(
                word,
            )
            == output
        )
