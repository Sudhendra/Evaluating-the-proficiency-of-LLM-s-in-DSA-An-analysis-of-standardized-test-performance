import pytest
from q_2623_memoize import Solution


@pytest.mark.parametrize(
    "output", [([4, 4, 1, 3, 2]), ("factorial", [2, 6, 2, 2, 6, 2]), ("fib", [8, 1])]
)
class TestSolution:
    def test_memoize(self, output: Any):
        sc = Solution()
        assert sc.memoize() == output
