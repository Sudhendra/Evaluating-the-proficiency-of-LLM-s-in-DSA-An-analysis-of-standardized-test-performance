import pytest
from q_0406_queueReconstructionByHeight import Solution


@pytest.mark.parametrize(
    "people, output",
    [
        (
            [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]],
            [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]],
        ),
        (
            [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]],
            [[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]],
        ),
    ],
)
class TestSolution:
    def test_reconstructQueue(self, people: List[List[int]], output: List[List[int]]):
        sc = Solution()
        assert (
            sc.reconstructQueue(
                people,
            )
            == output
        )
