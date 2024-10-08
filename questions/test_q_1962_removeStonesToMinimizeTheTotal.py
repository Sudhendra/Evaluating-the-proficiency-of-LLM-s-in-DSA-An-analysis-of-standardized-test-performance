import pytest
from q_1962_removeStonesToMinimizeTheTotal import Solution


@pytest.mark.parametrize(
    "piles, k, output", [([5, 4, 9], 2, 12), ([4, 3, 6, 7], 3, 12)]
)
class TestSolution:
    def test_minStoneSum(self, piles: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.minStoneSum(
                piles,
                k,
            )
            == output
        )
