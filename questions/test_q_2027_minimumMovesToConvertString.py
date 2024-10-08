import pytest
from q_2027_minimumMovesToConvertString import Solution


@pytest.mark.parametrize("s, output", [("XXX", 1), ("XXOX", 2), ("OOOO", 0)])
class TestSolution:
    def test_minimumMoves(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.minimumMoves(
                s,
            )
            == output
        )
