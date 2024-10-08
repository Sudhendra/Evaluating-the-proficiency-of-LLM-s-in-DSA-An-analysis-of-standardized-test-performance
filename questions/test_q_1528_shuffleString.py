import pytest
from q_1528_shuffleString import Solution


@pytest.mark.parametrize(
    "s, indices, output",
    [("codeleet", [4, 5, 6, 7, 0, 2, 1, 3], "leetcode"), ("abc", [0, 1, 2], "abc")],
)
class TestSolution:
    def test_restoreString(self, s: str, indices: List[int], output: str):
        sc = Solution()
        assert (
            sc.restoreString(
                s,
                indices,
            )
            == output
        )
