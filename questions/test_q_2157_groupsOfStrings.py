import pytest
from q_2157_groupsOfStrings import Solution


@pytest.mark.parametrize(
    "words, output", [(["a", "b", "ab", "cde"], [2, 3]), (["a", "ab", "abc"], [1, 3])]
)
class TestSolution:
    def test_groupStrings(self, words: List[str], output: List[int]):
        sc = Solution()
        assert (
            sc.groupStrings(
                words,
            )
            == output
        )
