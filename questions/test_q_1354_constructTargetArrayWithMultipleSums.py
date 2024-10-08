import pytest
from q_1354_constructTargetArrayWithMultipleSums import Solution


@pytest.mark.parametrize(
    "target, output", [([9, 3, 5], True), ([1, 1, 1, 2], False), ([8, 5], True)]
)
class TestSolution:
    def test_isPossible(self, target: List[int], output: bool):
        sc = Solution()
        assert (
            sc.isPossible(
                target,
            )
            == output
        )
