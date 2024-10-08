import pytest
from q_0806_numberOfLinesToWriteString import Solution


@pytest.mark.parametrize(
    "widths, s, output",
    [
        (
            [
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
            ],
            "abcdefghijklmnopqrstuvwxyz",
            [3, 60],
        ),
        (
            [
                4,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
                10,
            ],
            "bbbcccdddaaa",
            [2, 4],
        ),
    ],
)
class TestSolution:
    def test_numberOfLines(self, widths: List[int], s: str, output: List[int]):
        sc = Solution()
        assert (
            sc.numberOfLines(
                widths,
                s,
            )
            == output
        )
