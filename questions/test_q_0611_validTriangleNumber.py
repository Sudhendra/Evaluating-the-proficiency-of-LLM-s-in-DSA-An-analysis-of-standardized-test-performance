import pytest
from q_0611_validTriangleNumber import Solution


@pytest.mark.parametrize("nums, output", [([2, 2, 3, 4], 3), ([4, 2, 3, 4], 4)])
class TestSolution:
    def test_triangleNumber(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.triangleNumber(
                nums,
            )
            == output
        )
