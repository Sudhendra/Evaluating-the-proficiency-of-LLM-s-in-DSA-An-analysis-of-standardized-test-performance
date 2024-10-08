import pytest
from q_1621_numberOfSetsOfKNonOverlappingLineSegments import Solution


@pytest.mark.parametrize("n, k, output", [(4, 2, 5), (3, 1, 3), (30, 7, 796297179)])
class TestSolution:
    def test_numberOfSets(self, n: int, k: int, output: int):
        sc = Solution()
        assert (
            sc.numberOfSets(
                n,
                k,
            )
            == output
        )
