import pytest
from q_1460_makeTwoArraysEqualByReversingSubarrays import Solution


@pytest.mark.parametrize(
    "target, arr, output",
    [
        ([1, 2, 3, 4], [2, 4, 1, 3], True),
        ([7], [7], True),
        ([3, 7, 9], [3, 7, 11], False),
    ],
)
class TestSolution:
    def test_canBeEqual(self, target: List[int], arr: List[int], output: bool):
        sc = Solution()
        assert (
            sc.canBeEqual(
                target,
                arr,
            )
            == output
        )
