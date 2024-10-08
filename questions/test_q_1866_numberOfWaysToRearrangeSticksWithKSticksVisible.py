import pytest
from q_1866_numberOfWaysToRearrangeSticksWithKSticksVisible import Solution


@pytest.mark.parametrize("n, k, output", [(3, 2, 3), (5, 5, 1), (20, 11, 647427950)])
class TestSolution:
    def test_rearrangeSticks(self, n: int, k: int, output: int):
        sc = Solution()
        assert (
            sc.rearrangeSticks(
                n,
                k,
            )
            == output
        )
