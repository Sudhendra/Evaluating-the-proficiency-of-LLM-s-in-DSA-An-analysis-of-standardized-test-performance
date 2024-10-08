import pytest
from q_0066_plusOne import Solution


@pytest.mark.parametrize(
    "digits, output",
    [([1, 2, 3], [1, 2, 4]), ([4, 3, 2, 1], [4, 3, 2, 2]), ([9], [1, 0])],
)
class TestSolution:
    def test_plusOne(self, digits: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.plusOne(
                digits,
            )
            == output
        )
