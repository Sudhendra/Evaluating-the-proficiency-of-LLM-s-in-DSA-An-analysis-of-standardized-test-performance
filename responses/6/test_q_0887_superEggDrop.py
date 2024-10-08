import pytest
from q_0887_superEggDrop import Solution


@pytest.mark.parametrize("k, n, output", [(1, 2, 2), (2, 6, 3), (3, 14, 4)])
class TestSolution:
    def test_superEggDrop(self, k: int, n: int, output: int):
        sc = Solution()
        assert (
            sc.superEggDrop(
                k,
                n,
            )
            == output
        )
