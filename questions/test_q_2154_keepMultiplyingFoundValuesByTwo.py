import pytest
from q_2154_keepMultiplyingFoundValuesByTwo import Solution


@pytest.mark.parametrize(
    "nums, original, output", [([5, 3, 6, 1, 12], 3, 24), ([2, 7, 9], 4, 4)]
)
class TestSolution:
    def test_findFinalValue(self, nums: List[int], original: int, output: int):
        sc = Solution()
        assert (
            sc.findFinalValue(
                nums,
                original,
            )
            == output
        )
