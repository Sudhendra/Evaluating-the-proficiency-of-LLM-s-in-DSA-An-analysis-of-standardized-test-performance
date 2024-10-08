import pytest
from q_2741_specialPermutations import Solution


@pytest.mark.parametrize("nums, output", [([2, 3, 6], 2), ([1, 4, 3], 2)])
class TestSolution:
    def test_specialPerm(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.specialPerm(
                nums,
            )
            == output
        )
