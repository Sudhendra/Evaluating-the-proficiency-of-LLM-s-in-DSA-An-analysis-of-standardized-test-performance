import pytest
from q_0920_numberOfMusicPlaylists import Solution


@pytest.mark.parametrize(
    "n, goal, k, output", [(3, 3, 1, 6), (2, 3, 0, 6), (2, 3, 1, 2)]
)
class TestSolution:
    def test_numMusicPlaylists(self, n: int, goal: int, k: int, output: int):
        sc = Solution()
        assert (
            sc.numMusicPlaylists(
                n,
                goal,
                k,
            )
            == output
        )
