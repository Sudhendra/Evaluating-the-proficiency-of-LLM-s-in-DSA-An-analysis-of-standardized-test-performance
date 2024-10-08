import pytest
from q_2637_promiseTimeLimit import Solution


@pytest.mark.parametrize(
    "output",
    [
        ({"rejected": "Time Limit Exceeded", "time": 50}),
        ({"resolved": 25, "time": 100}),
        ({"resolved": 15, "time": 120}),
        ({"rejected": "Error", "time": 0}),
    ],
)
class TestSolution:
    def test_promiseTimeLimit(self, output: Any):
        sc = Solution()
        assert sc.promiseTimeLimit() == output
