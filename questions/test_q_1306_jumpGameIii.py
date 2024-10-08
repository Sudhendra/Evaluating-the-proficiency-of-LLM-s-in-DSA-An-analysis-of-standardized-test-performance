import pytest
from q_1306_jumpGameIii import Solution


@pytest.mark.parametrize(
    "arr, start, output",
    [
        ([4, 2, 3, 0, 3, 1, 2], 5, True),
        ([4, 2, 3, 0, 3, 1, 2], 0, True),
        ([3, 0, 2, 1, 2], 2, False),
    ],
)
class TestSolution:
    def test_canReach(self, arr: List[int], start: int, output: bool):
        sc = Solution()
        assert (
            sc.canReach(
                arr,
                start,
            )
            == output
        )
