import pytest
from q_3021_aliceAndBobPlayingFlowerGame import Solution


@pytest.mark.parametrize("n, m, output", [(3, 2, 3), (1, 1, 0)])
class TestSolution:
    def test_flowerGame(self, n: int, m: int, output: int):
        sc = Solution()
        assert (
            sc.flowerGame(
                n,
                m,
            )
            == output
        )
