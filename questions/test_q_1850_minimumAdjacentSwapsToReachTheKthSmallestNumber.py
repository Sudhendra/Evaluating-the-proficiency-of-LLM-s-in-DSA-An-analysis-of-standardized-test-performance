import pytest
from q_1850_minimumAdjacentSwapsToReachTheKthSmallestNumber import Solution


@pytest.mark.parametrize(
    "num, k, output", [("5489355142", 4, 2), ("11112", 4, 4), ("00123", 1, 1)]
)
class TestSolution:
    def test_getMinSwaps(self, num: str, k: int, output: int):
        sc = Solution()
        assert (
            sc.getMinSwaps(
                num,
                k,
            )
            == output
        )
