import pytest
from q_1654_minimumJumpsToReachHome import Solution


@pytest.mark.parametrize(
    "forbidden, a, b, x, output",
    [
        ([14, 4, 18, 1, 15], 3, 15, 9, 3),
        ([8, 3, 16, 6, 12, 20], 15, 13, 11, -1),
        ([1, 6, 2, 14, 5, 17, 4], 16, 9, 7, 2),
    ],
)
class TestSolution:
    def test_minimumJumps(
        self, forbidden: List[int], a: int, b: int, x: int, output: int
    ):
        sc = Solution()
        assert (
            sc.minimumJumps(
                forbidden,
                a,
                b,
                x,
            )
            == output
        )
