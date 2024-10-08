import pytest
from q_2630_memoizeIi import Solution


@pytest.mark.parametrize(
    "output",
    [
        ([{"val": 4, "calls": 1}, {"val": 4, "calls": 1}, {"val": 3, "calls": 2}]),
        ([{"val": {}, "calls": 1}, {"val": {}, "calls": 2}, {"val": {}, "calls": 3}]),
        ([{"val": {}, "calls": 1}, {"val": {}, "calls": 1}, {"val": {}, "calls": 1}]),
    ],
)
class TestSolution:
    def test_memoizeIi(self, output: Any):
        sc = Solution()
        assert sc.memoizeIi() == output
