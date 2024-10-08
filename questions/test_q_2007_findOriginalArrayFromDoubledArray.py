import pytest
from q_2007_findOriginalArrayFromDoubledArray import Solution


@pytest.mark.parametrize(
    "changed, output", [([1, 3, 4, 2, 6, 8], [1, 3, 4]), ([6, 3, 0, 1], []), ([1], [])]
)
class TestSolution:
    def test_findOriginalArray(self, changed: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.findOriginalArray(
                changed,
            )
            == output
        )
