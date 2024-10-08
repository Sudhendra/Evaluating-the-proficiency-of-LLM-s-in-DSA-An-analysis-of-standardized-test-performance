import pytest
from q_1722_minimizeHammingDistanceAfterSwapOperations import Solution


@pytest.mark.parametrize(
    "source, target, allowedSwaps, output",
    [
        ([1, 2, 3, 4], [2, 1, 4, 5], [[0, 1], [2, 3]], 1),
        ([1, 2, 3, 4], [1, 3, 2, 4], [], 2),
        ([5, 1, 2, 4, 3], [1, 5, 4, 2, 3], [[0, 4], [4, 2], [1, 3], [1, 4]], 0),
    ],
)
class TestSolution:
    def test_minimumHammingDistance(
        self,
        source: List[int],
        target: List[int],
        allowedSwaps: List[List[int]],
        output: int,
    ):
        sc = Solution()
        assert (
            sc.minimumHammingDistance(
                source,
                target,
                allowedSwaps,
            )
            == output
        )
