import pytest
from q_1486_xorOperationInAnArray import Solution


@pytest.mark.parametrize("n, start, output", [(5, 0, 8), (4, 3, 8)])
class TestSolution:
    def test_xorOperation(self, n: int, start: int, output: int):
        sc = Solution()
        assert (
            sc.xorOperation(
                n,
                start,
            )
            == output
        )
