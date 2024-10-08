import pytest
from q_1943_describeThePainting import Solution


@pytest.mark.parametrize(
    "segments, output",
    [
        ([[1, 4, 5], [4, 7, 7], [1, 7, 9]], [[1, 4, 14], [4, 7, 16]]),
        (
            [[1, 7, 9], [6, 8, 15], [8, 10, 7]],
            [[1, 6, 9], [6, 7, 24], [7, 8, 15], [8, 10, 7]],
        ),
        ([[1, 4, 5], [1, 4, 7], [4, 7, 1], [4, 7, 11]], [[1, 4, 12], [4, 7, 12]]),
    ],
)
class TestSolution:
    def test_splitPainting(self, segments: List[List[int]], output: List[List[int]]):
        sc = Solution()
        assert (
            sc.splitPainting(
                segments,
            )
            == output
        )
