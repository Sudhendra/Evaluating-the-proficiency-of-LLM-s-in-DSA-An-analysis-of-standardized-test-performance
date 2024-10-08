import pytest
from q_1130_minimumCostTreeFromLeafValues import Solution


@pytest.mark.parametrize("arr, output", [([6, 2, 4], 32), ([4, 11], 44)])
class TestSolution:
    def test_mctFromLeafValues(self, arr: List[int], output: int):
        sc = Solution()
        assert (
            sc.mctFromLeafValues(
                arr,
            )
            == output
        )
