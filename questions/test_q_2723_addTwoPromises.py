import pytest
from q_2723_addTwoPromises import Solution


@pytest.mark.parametrize("output", [(7), (-2)])
class TestSolution:
    def test_addTwoPromises(self, output: Any):
        sc = Solution()
        assert sc.addTwoPromises() == output
