import pytest
from q_1128_numberOfEquivalentDominoPairs import Solution


@pytest.mark.parametrize(
    "dominoes, output",
    [
        ([[1, 2], [2, 1], [3, 4], [5, 6]], 1),
        ([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]], 3),
    ],
)
class TestSolution:
    def test_numEquivDominoPairs(self, dominoes: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.numEquivDominoPairs(
                dominoes,
            )
            == output
        )
