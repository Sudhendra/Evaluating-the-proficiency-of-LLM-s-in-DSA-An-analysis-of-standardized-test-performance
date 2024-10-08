import pytest
from q_0969_pancakeSorting import Solution


@pytest.mark.parametrize("arr, output", [([3, 2, 4, 1], [4, 2, 4, 3]), ([1, 2, 3], [])])
class TestSolution:
    def test_pancakeSort(self, arr: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.pancakeSort(
                arr,
            )
            == output
        )
