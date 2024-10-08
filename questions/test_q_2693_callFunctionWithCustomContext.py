import pytest
from q_2693_callFunctionWithCustomContext import Solution


@pytest.mark.parametrize("output", [(12), ("The cost of the burger is 11")])
class TestSolution:
    def test_callFunctionWithCustomContext(self, output: Any):
        sc = Solution()
        assert sc.callFunctionWithCustomContext() == output
