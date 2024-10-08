import pytest
from q_1503_lastMomentBeforeAllAntsFallOutOfAPlank import Solution


@pytest.mark.parametrize(
    "n, left, right, output",
    [
        (4, [4, 3], [0, 1], 4),
        (7, [], [0, 1, 2, 3, 4, 5, 6, 7], 7),
        (7, [0, 1, 2, 3, 4, 5, 6, 7], [], 7),
    ],
)
class TestSolution:
    def test_getLastMoment(
        self, n: int, left: List[int], right: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.getLastMoment(
                n,
                left,
                right,
            )
            == output
        )
