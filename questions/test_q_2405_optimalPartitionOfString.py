import pytest
from q_2405_optimalPartitionOfString import Solution


@pytest.mark.parametrize("s, output", [("abacaba", 4), ("ssssss", 6)])
class TestSolution:
    def test_partitionString(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.partitionString(
                s,
            )
            == output
        )
