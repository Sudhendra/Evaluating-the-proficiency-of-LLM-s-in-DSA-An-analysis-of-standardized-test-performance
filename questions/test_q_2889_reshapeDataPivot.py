import pytest
from q_2889_reshapeDataPivot import Solution


@pytest.mark.parametrize("output", [(None)])
class TestSolution:
    def test_reshapeDataPivot(self, output: Any):
        sc = Solution()
        assert sc.reshapeDataPivot() == output
