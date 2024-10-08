import pytest
from q_1025_divisorGame import Solution


@pytest.mark.parametrize("n, output", [(2, True), (3, False)])
class TestSolution:
    def test_divisorGame(self, n: int, output: bool):
        sc = Solution()
        assert (
            sc.divisorGame(
                n,
            )
            == output
        )
