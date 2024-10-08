import pytest
from q_1689_partitioningIntoMinimumNumberOfDeciBinaryNumbers import Solution


@pytest.mark.parametrize(
    "n, output", [("32", 3), ("82734", 8), ("27346209830709182346", 9)]
)
class TestSolution:
    def test_minPartitions(self, n: str, output: int):
        sc = Solution()
        assert (
            sc.minPartitions(
                n,
            )
            == output
        )
