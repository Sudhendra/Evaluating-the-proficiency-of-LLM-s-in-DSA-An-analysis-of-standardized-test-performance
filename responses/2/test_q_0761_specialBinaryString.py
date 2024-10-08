import pytest
from q_0761_specialBinaryString import Solution


@pytest.mark.parametrize("s, output", [("11011000", "11100100"), ("10", "10")])
class TestSolution:
    def test_makeLargestSpecial(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.makeLargestSpecial(
                s,
            )
            == output
        )
