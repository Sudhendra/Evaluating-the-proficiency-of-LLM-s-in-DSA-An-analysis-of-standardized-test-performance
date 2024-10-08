import pytest
from q_0775_globalAndLocalInversions import Solution


@pytest.mark.parametrize("nums, output", [([1, 0, 2], True), ([1, 2, 0], False)])
class TestSolution:
    def test_isIdealPermutation(self, nums: List[int], output: bool):
        sc = Solution()
        assert (
            sc.isIdealPermutation(
                nums,
            )
            == output
        )
