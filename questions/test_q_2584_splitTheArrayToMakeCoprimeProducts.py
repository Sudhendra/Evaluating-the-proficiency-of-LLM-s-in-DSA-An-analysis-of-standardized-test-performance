import pytest
from q_2584_splitTheArrayToMakeCoprimeProducts import Solution


@pytest.mark.parametrize(
    "nums, output", [([4, 7, 8, 15, 3, 5], 2), ([4, 7, 15, 8, 3, 5], -1)]
)
class TestSolution:
    def test_findValidSplit(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.findValidSplit(
                nums,
            )
            == output
        )
