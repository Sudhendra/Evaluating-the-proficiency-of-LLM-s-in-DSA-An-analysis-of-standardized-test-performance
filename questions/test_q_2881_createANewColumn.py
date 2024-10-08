import pytest
from q_2881_createANewColumn import Solution


@pytest.mark.parametrize("output", [(None)])
class TestSolution:
    def test_createANewColumn(self, output: Any):
        sc = Solution()
        assert sc.createANewColumn() == output
