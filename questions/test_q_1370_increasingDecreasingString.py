import pytest
from q_1370_increasingDecreasingString import Solution


@pytest.mark.parametrize(
    "s, output", [("aaaabbbbcccc", "abccbaabccba"), ("rat", "art")]
)
class TestSolution:
    def test_sortString(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.sortString(
                s,
            )
            == output
        )
