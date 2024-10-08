import pytest
from q_2351_firstLetterToAppearTwice import Solution


@pytest.mark.parametrize("s, output", [("abccbaacz", "c"), ("abcdd", "d")])
class TestSolution:
    def test_repeatedCharacter(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.repeatedCharacter(
                s,
            )
            == output
        )
