import pytest
from q_1239_maximumLengthOfAConcatenatedStringWithUniqueCharacters import Solution


@pytest.mark.parametrize(
    "arr, output",
    [
        (["un", "iq", "ue"], 4),
        (["cha", "r", "act", "ers"], 6),
        (["abcdefghijklmnopqrstuvwxyz"], 26),
    ],
)
class TestSolution:
    def test_maxLength(self, arr: List[str], output: int):
        sc = Solution()
        assert (
            sc.maxLength(
                arr,
            )
            == output
        )
