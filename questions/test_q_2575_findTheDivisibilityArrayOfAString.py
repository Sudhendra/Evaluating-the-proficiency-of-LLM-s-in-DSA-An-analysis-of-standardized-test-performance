import pytest
from q_2575_findTheDivisibilityArrayOfAString import Solution


@pytest.mark.parametrize(
    "word, m, output",
    [("998244353", 3, [1, 1, 0, 0, 0, 1, 1, 0, 0]), ("1010", 10, [0, 1, 0, 1])],
)
class TestSolution:
    def test_divisibilityArray(self, word: str, m: int, output: List[int]):
        sc = Solution()
        assert (
            sc.divisibilityArray(
                word,
                m,
            )
            == output
        )
