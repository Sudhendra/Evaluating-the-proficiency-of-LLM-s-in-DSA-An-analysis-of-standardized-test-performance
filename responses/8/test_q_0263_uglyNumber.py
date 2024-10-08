import pytest
from q_0263_uglyNumber import Solution


@pytest.mark.parametrize("n, output", [(6, True), (1, True), (14, False)])
class TestSolution:
    def test_isUgly(self, n: int, output: bool):
        sc = Solution()
        assert (
            sc.isUgly(
                n,
            )
            == output
        )
