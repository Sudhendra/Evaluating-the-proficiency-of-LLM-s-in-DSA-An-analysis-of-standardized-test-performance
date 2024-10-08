import pytest
from q_0823_binaryTreesWithFactors import Solution


@pytest.mark.parametrize("arr, output", [([2, 4], 3), ([2, 4, 5, 10], 7)])
class TestSolution:
    def test_numFactoredBinaryTrees(self, arr: List[int], output: int):
        sc = Solution()
        assert (
            sc.numFactoredBinaryTrees(
                arr,
            )
            == output
        )
