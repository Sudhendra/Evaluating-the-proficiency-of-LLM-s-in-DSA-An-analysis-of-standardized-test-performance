import pytest
from q_0875_kokoEatingBananas import Solution


@pytest.mark.parametrize(
    "piles, h, output",
    [([3, 6, 7, 11], 8, 4), ([30, 11, 23, 4, 20], 5, 30), ([30, 11, 23, 4, 20], 6, 23)],
)
class TestSolution:
    def test_minEatingSpeed(self, piles: List[int], h: int, output: int):
        sc = Solution()
        assert (
            sc.minEatingSpeed(
                piles,
                h,
            )
            == output
        )
