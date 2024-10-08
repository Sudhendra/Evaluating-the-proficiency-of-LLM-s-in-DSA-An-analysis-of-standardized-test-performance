import pytest
from q_0975_oddEvenJump import Solution


@pytest.mark.parametrize(
    "arr, output",
    [([10, 13, 12, 14, 15], 2), ([2, 3, 1, 1, 4], 3), ([5, 1, 3, 4, 2], 3)],
)
class TestSolution:
    def test_oddEvenJumps(self, arr: List[int], output: int):
        sc = Solution()
        assert (
            sc.oddEvenJumps(
                arr,
            )
            == output
        )
