import pytest
from q_1311_getWatchedVideosByYourFriends import Solution


@pytest.mark.parametrize(
    "watchedVideos, friends, id, level, output",
    [
        (
            [["A", "B"], ["C"], ["B", "C"], ["D"]],
            [[1, 2], [0, 3], [0, 3], [1, 2]],
            0,
            1,
            ["B", "C"],
        ),
        (
            [["A", "B"], ["C"], ["B", "C"], ["D"]],
            [[1, 2], [0, 3], [0, 3], [1, 2]],
            0,
            2,
            ["D"],
        ),
    ],
)
class TestSolution:
    def test_watchedVideosByFriends(
        self,
        watchedVideos: List[List[str]],
        friends: List[List[int]],
        id: int,
        level: int,
        output: List[str],
    ):
        sc = Solution()
        assert (
            sc.watchedVideosByFriends(
                watchedVideos,
                friends,
                id,
                level,
            )
            == output
        )
