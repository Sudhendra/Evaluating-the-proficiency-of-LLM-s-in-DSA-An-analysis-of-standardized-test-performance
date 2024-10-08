import pytest
from q_2626_arrayReduceTransformation import Solution


@pytest.mark.parametrize("output", [(10), (130), (25)])
class TestSolution:
    def test_arrayReduceTransformation(self, output: Any):
        sc = Solution()
        assert sc.arrayReduceTransformation() == output
