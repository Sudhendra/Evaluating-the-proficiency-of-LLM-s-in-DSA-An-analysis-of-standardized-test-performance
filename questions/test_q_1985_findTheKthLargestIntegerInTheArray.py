import pytest
from q_1985_findTheKthLargestIntegerInTheArray import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [
        (["3", "6", "7", "10"], 4, "3"),
        (["2", "21", "12", "1"], 3, "2"),
        (["0", "0"], 2, "0"),
    ],
)
class TestSolution:
    def test_kthLargestNumber(self, nums: List[str], k: int, output: str):
        sc = Solution()
        assert (
            sc.kthLargestNumber(
                nums,
                k,
            )
            == output
        )
