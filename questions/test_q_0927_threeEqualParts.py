import pytest
from q_0927_threeEqualParts import Solution


@pytest.mark.parametrize(
    "arr, output",
    [([1, 0, 1, 0, 1], [0, 3]), ([1, 1, 0, 1, 1], [-1, -1]), ([1, 1, 0, 0, 1], [0, 2])],
)
class TestSolution:
    def test_threeEqualParts(self, arr: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.threeEqualParts(
                arr,
            )
            == output
        )
