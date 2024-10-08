import pytest
from q_2839_checkIfStringsCanBeMadeEqualWithOperationsI import Solution


@pytest.mark.parametrize(
    "s1, s2, output", [("abcd", "cdab", True), ("abcd", "dacb", False)]
)
class TestSolution:
    def test_canBeEqual(self, s1: str, s2: str, output: bool):
        sc = Solution()
        assert (
            sc.canBeEqual(
                s1,
                s2,
            )
            == output
        )
