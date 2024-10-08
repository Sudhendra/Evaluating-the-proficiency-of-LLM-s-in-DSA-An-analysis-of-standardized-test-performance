import pytest
from q_0014_longestCommonPrefix import Solution


@pytest.mark.parametrize(
    "strs, output",
    [(["flower", "flow", "flight"], "fl"), (["dog", "racecar", "car"], "")],
)
class TestSolution:
    def test_longestCommonPrefix(self, strs: List[str], output: str):
        sc = Solution()
        assert (
            sc.longestCommonPrefix(
                strs,
            )
            == output
        )
