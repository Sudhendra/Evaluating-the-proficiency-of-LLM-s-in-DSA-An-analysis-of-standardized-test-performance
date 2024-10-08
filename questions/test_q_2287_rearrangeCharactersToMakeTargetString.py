import pytest
from q_2287_rearrangeCharactersToMakeTargetString import Solution


@pytest.mark.parametrize(
    "s, target, output",
    [
        ("ilovecodingonleetcode", "code", 2),
        ("abcba", "abc", 1),
        ("abbaccaddaeea", "aaaaa", 1),
    ],
)
class TestSolution:
    def test_rearrangeCharacters(self, s: str, target: str, output: int):
        sc = Solution()
        assert (
            sc.rearrangeCharacters(
                s,
                target,
            )
            == output
        )
