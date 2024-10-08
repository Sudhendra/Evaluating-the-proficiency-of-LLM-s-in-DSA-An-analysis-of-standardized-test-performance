import pytest
from q_0665_nonDecreasingArray import Solution


@pytest.mark.parametrize("nums, output", [([4, 2, 3], True), ([4, 2, 1], False)])
class TestSolution:
    def test_checkPossibility(self, nums: List[int], output: bool):
        sc = Solution()
        assert (
            sc.checkPossibility(
                nums,
            )
            == output
        )
