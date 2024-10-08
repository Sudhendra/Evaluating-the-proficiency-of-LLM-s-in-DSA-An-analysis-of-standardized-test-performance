import pytest
from q_2138_divideAStringIntoGroupsOfSizeK import Solution


@pytest.mark.parametrize(
    "s, k, fill, output",
    [
        ("abcdefghi", 3, "x", ["abc", "def", "ghi"]),
        ("abcdefghij", 3, "x", ["abc", "def", "ghi", "jxx"]),
    ],
)
class TestSolution:
    def test_divideString(self, s: str, k: int, fill: str, output: List[str]):
        sc = Solution()
        assert (
            sc.divideString(
                s,
                k,
                fill,
            )
            == output
        )
