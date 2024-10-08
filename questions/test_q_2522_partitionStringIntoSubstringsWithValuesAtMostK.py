import pytest
from q_2522_partitionStringIntoSubstringsWithValuesAtMostK import Solution


@pytest.mark.parametrize("s, k, output", [("165462", 60, 4), ("238182", 5, -1)])
class TestSolution:
    def test_minimumPartition(self, s: str, k: int, output: int):
        sc = Solution()
        assert (
            sc.minimumPartition(
                s,
                k,
            )
            == output
        )
