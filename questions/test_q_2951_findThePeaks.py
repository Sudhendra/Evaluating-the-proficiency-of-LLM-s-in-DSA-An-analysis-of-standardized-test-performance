import pytest
from q_2951_findThePeaks import Solution


@pytest.mark.parametrize(
    "mountain, output", [([2, 4, 4], []), ([1, 4, 3, 8, 5], [1, 3])]
)
class TestSolution:
    def test_findPeaks(self, mountain: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.findPeaks(
                mountain,
            )
            == output
        )
