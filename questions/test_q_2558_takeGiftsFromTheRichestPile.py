import pytest
from q_2558_takeGiftsFromTheRichestPile import Solution


@pytest.mark.parametrize(
    "gifts, k, output", [([25, 64, 9, 4, 100], 4, 29), ([1, 1, 1, 1], 4, 4)]
)
class TestSolution:
    def test_pickGifts(self, gifts: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.pickGifts(
                gifts,
                k,
            )
            == output
        )
