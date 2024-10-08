import pytest
from q_1889_minimumSpaceWastedFromPackaging import Solution


@pytest.mark.parametrize(
    "packages, boxes, output",
    [
        ([2, 3, 5], [[4, 8], [2, 8]], 6),
        ([2, 3, 5], [[1, 4], [2, 3], [3, 4]], -1),
        ([3, 5, 8, 10, 11, 12], [[12], [11, 9], [10, 5, 14]], 9),
    ],
)
class TestSolution:
    def test_minWastedSpace(
        self, packages: List[int], boxes: List[List[int]], output: int
    ):
        sc = Solution()
        assert (
            sc.minWastedSpace(
                packages,
                boxes,
            )
            == output
        )
