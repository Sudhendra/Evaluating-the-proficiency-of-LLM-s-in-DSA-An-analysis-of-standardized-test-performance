import pytest
from q_1534_countGoodTriplets import Solution


@pytest.mark.parametrize(
    "arr, a, b, c, output",
    [([3, 0, 1, 1, 9, 7], 7, 2, 3, 4), ([1, 1, 2, 2, 3], 0, 0, 1, 0)],
)
class TestSolution:
    def test_countGoodTriplets(
        self, arr: List[int], a: int, b: int, c: int, output: int
    ):
        sc = Solution()
        assert (
            sc.countGoodTriplets(
                arr,
                a,
                b,
                c,
            )
            == output
        )
