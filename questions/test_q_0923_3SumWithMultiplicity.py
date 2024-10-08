import pytest
from q_0923_3SumWithMultiplicity import Solution


@pytest.mark.parametrize(
    "arr, target, output",
    [
        ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8, 20),
        ([1, 1, 2, 2, 2, 2], 5, 12),
        ([2, 1, 3], 6, 1),
    ],
)
class TestSolution:
    def test_threeSumMulti(self, arr: List[int], target: int, output: int):
        sc = Solution()
        assert (
            sc.threeSumMulti(
                arr,
                target,
            )
            == output
        )
