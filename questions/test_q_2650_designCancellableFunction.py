import pytest
from q_2650_designCancellableFunction import Solution


@pytest.mark.parametrize(
    "output",
    [
        ({"resolved": 42}),
        ({"rejected": "Error: Hello"}),
        ({"rejected": "Cancelled"}),
        ({"resolved": 2}),
        ({"resolved": 1}),
        ({"resolved": 4}),
    ],
)
class TestSolution:
    def test_designCancellableFunction(self, output: Any):
        sc = Solution()
        assert sc.designCancellableFunction() == output
