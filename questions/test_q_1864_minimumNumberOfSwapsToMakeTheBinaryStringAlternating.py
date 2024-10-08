import pytest
from q_1864_minimumNumberOfSwapsToMakeTheBinaryStringAlternating import Solution


@pytest.mark.parametrize("s, output", [("111000", 1), ("010", 0), ("1110", -1)])
class TestSolution:
    def test_minSwaps(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.minSwaps(
                s,
            )
            == output
        )
