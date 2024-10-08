import pytest
from q_2680_maximumOr import Solution


@pytest.mark.parametrize("nums, k, output", [([12, 9], 1, 30), ([8, 1, 2], 2, 35)])
class TestSolution:
    def test_maximumOr(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.maximumOr(
                nums,
                k,
            )
            == output
        )
