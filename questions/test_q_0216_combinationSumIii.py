import pytest
from q_0216_combinationSumIii import Solution


@pytest.mark.parametrize(
    "k, n, output",
    [(3, 7, [[1, 2, 4]]), (3, 9, [[1, 2, 6], [1, 3, 5], [2, 3, 4]]), (4, 1, [])],
)
class TestSolution:
    def test_combinationSum3(self, k: int, n: int, output: List[List[int]]):
        sc = Solution()
        assert (
            sc.combinationSum3(
                k,
                n,
            )
            == output
        )
