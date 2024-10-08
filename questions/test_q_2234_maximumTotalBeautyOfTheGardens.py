import pytest
from q_2234_maximumTotalBeautyOfTheGardens import Solution


@pytest.mark.parametrize(
    "flowers, newFlowers, target, full, partial, output",
    [([1, 3, 1, 1], 7, 6, 12, 1, 14), ([2, 4, 5, 3], 10, 5, 2, 6, 30)],
)
class TestSolution:
    def test_maximumBeauty(
        self,
        flowers: List[int],
        newFlowers: int,
        target: int,
        full: int,
        partial: int,
        output: int,
    ):
        sc = Solution()
        assert (
            sc.maximumBeauty(
                flowers,
                newFlowers,
                target,
                full,
                partial,
            )
            == output
        )
