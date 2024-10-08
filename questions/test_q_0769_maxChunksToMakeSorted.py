import pytest
from q_0769_maxChunksToMakeSorted import Solution


@pytest.mark.parametrize("arr, output", [([4, 3, 2, 1, 0], 1), ([1, 0, 2, 3, 4], 4)])
class TestSolution:
    def test_maxChunksToSorted(self, arr: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxChunksToSorted(
                arr,
            )
            == output
        )
