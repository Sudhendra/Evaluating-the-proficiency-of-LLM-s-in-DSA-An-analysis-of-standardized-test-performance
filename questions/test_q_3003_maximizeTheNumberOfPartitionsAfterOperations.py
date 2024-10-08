import pytest
from q_3003_maximizeTheNumberOfPartitionsAfterOperations import Solution


@pytest.mark.parametrize(
    "s, k, output", [("accca", 2, 3), ("aabaab", 3, 1), ("xxyz", 1, 4)]
)
class TestSolution:
    def test_maxPartitionsAfterOperations(self, s: str, k: int, output: int):
        sc = Solution()
        assert (
            sc.maxPartitionsAfterOperations(
                s,
                k,
            )
            == output
        )
