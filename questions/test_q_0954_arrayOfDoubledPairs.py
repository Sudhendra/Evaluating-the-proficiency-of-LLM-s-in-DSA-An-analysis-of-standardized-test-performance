import pytest
from q_0954_arrayOfDoubledPairs import Solution


@pytest.mark.parametrize(
    "arr, output",
    [([3, 1, 3, 6], False), ([2, 1, 2, 6], False), ([4, -2, 2, -4], True)],
)
class TestSolution:
    def test_canReorderDoubled(self, arr: List[int], output: bool):
        sc = Solution()
        assert (
            sc.canReorderDoubled(
                arr,
            )
            == output
        )
