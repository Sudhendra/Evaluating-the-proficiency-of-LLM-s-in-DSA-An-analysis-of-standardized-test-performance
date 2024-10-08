import pytest
from q_2896_applyOperationsToMakeTwoStringsEqual import Solution


@pytest.mark.parametrize(
    "s1, s2, x, output", [("1100011000", "0101001010", 2, 4), ("10110", "00011", 4, -1)]
)
class TestSolution:
    def test_minOperations(self, s1: str, s2: str, x: int, output: int):
        sc = Solution()
        assert (
            sc.minOperations(
                s1,
                s2,
                x,
            )
            == output
        )
