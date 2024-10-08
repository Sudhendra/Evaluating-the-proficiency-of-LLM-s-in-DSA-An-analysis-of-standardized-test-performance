import pytest
from q_3024_typeOfTriangle import Solution


@pytest.mark.parametrize(
    "nums, output", [([3, 3, 3], "equilateral"), ([3, 4, 5], "scalene")]
)
class TestSolution:
    def test_triangleType(self, nums: List[int], output: str):
        sc = Solution()
        assert (
            sc.triangleType(
                nums,
            )
            == output
        )
