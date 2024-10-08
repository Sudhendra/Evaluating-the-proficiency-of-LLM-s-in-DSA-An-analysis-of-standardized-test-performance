import pytest
from q_1415_theKThLexicographicalStringOfAllHappyStringsOfLengthN import Solution


@pytest.mark.parametrize("n, k, output", [(1, 3, "c"), (1, 4, ""), (3, 9, "cab")])
class TestSolution:
    def test_getHappyString(self, n: int, k: int, output: str):
        sc = Solution()
        assert (
            sc.getHappyString(
                n,
                k,
            )
            == output
        )
