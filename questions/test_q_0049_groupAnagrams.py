import pytest
from q_0049_groupAnagrams import Solution


@pytest.mark.parametrize(
    "strs, output",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ],
)
class TestSolution:
    def test_groupAnagrams(self, strs: List[str], output: List[List[str]]):
        sc = Solution()
        assert (
            sc.groupAnagrams(
                strs,
            )
            == output
        )
