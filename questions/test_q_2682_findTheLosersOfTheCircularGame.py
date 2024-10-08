import pytest
from q_2682_findTheLosersOfTheCircularGame import Solution


@pytest.mark.parametrize("n, k, output", [(5, 2, [4, 5]), (4, 4, [2, 3, 4])])
class TestSolution:
    def test_circularGameLosers(self, n: int, k: int, output: List[int]):
        sc = Solution()
        assert (
            sc.circularGameLosers(
                n,
                k,
            )
            == output
        )
