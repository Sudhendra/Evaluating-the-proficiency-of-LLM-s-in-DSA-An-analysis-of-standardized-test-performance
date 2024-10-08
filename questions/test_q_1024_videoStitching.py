import pytest
from q_1024_videoStitching import Solution


@pytest.mark.parametrize(
    "clips, time, output",
    [
        ([[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10, 3),
        ([[0, 1], [1, 2]], 5, -1),
        (
            [
                [0, 1],
                [6, 8],
                [0, 2],
                [5, 6],
                [0, 4],
                [0, 3],
                [6, 7],
                [1, 3],
                [4, 7],
                [1, 4],
                [2, 5],
                [2, 6],
                [3, 4],
                [4, 5],
                [5, 7],
                [6, 9],
            ],
            9,
            3,
        ),
    ],
)
class TestSolution:
    def test_videoStitching(self, clips: List[List[int]], time: int, output: int):
        sc = Solution()
        assert (
            sc.videoStitching(
                clips,
                time,
            )
            == output
        )
