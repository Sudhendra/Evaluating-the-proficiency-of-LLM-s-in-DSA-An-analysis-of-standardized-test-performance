import pytest
from q_0763_partitionLabels import Solution


@pytest.mark.parametrize(
    "s, output", [("ababcbacadefegdehijhklij", [9, 7, 8]), ("eccbbbbdec", [10])]
)
class TestSolution:
    def test_partitionLabels(self, s: str, output: List[int]):
        sc = Solution()
        assert (
            sc.partitionLabels(
                s,
            )
            == output
        )
