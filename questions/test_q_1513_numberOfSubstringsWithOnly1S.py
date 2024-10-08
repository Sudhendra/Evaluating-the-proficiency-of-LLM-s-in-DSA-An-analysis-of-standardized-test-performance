import pytest
from q_1513_numberOfSubstringsWithOnly1S import Solution


@pytest.mark.parametrize("s, output", [("0110111", 9), ("101", 2), ("111111", 21)])
class TestSolution:
    def test_numSub(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.numSub(
                s,
            )
            == output
        )
