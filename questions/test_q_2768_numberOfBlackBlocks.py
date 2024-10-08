import pytest
from q_2768_numberOfBlackBlocks import Solution


@pytest.mark.parametrize(
    "m, n, coordinates, output",
    [
        (3, 3, [[0, 0]], [3, 1, 0, 0, 0]),
        (3, 3, [[0, 0], [1, 1], [0, 2]], [0, 2, 2, 0, 0]),
    ],
)
class TestSolution:
    def test_countBlackBlocks(
        self, m: int, n: int, coordinates: List[List[int]], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.countBlackBlocks(
                m,
                n,
                coordinates,
            )
            == output
        )
