import pytest
from q_1643_kthSmallestInstructions import Solution


@pytest.mark.parametrize(
    "destination, k, output",
    [([2, 3], 1, "HHHVV"), ([2, 3], 2, "HHVHV"), ([2, 3], 3, "HHVVH")],
)
class TestSolution:
    def test_kthSmallestPath(self, destination: List[int], k: int, output: str):
        sc = Solution()
        assert (
            sc.kthSmallestPath(
                destination,
                k,
            )
            == output
        )
