import pytest
from q_1649_createSortedArrayThroughInstructions import Solution


@pytest.mark.parametrize(
    "instructions, output",
    [([1, 5, 6, 2], 1), ([1, 2, 3, 6, 5, 4], 3), ([1, 3, 3, 3, 2, 4, 2, 1, 2], 4)],
)
class TestSolution:
    def test_createSortedArray(self, instructions: List[int], output: int):
        sc = Solution()
        assert (
            sc.createSortedArray(
                instructions,
            )
            == output
        )
