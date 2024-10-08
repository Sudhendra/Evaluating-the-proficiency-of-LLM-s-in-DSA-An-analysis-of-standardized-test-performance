import pytest
from q_0567_permutationInString import Solution


@pytest.mark.parametrize(
    "s1, s2, output", [("ab", "eidbaooo", True), ("ab", "eidboaoo", False)]
)
class TestSolution:
    def test_checkInclusion(self, s1: str, s2: str, output: bool):
        sc = Solution()
        assert (
            sc.checkInclusion(
                s1,
                s2,
            )
            == output
        )
