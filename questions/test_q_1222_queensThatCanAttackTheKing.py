import pytest
from q_1222_queensThatCanAttackTheKing import Solution


@pytest.mark.parametrize(
    "queens, king, output",
    [
        (
            [[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]],
            [0, 0],
            [[0, 1], [1, 0], [3, 3]],
        ),
        (
            [[0, 0], [1, 1], [2, 2], [3, 4], [3, 5], [4, 4], [4, 5]],
            [3, 3],
            [[2, 2], [3, 4], [4, 4]],
        ),
    ],
)
class TestSolution:
    def test_queensAttacktheKing(
        self, queens: List[List[int]], king: List[int], output: List[List[int]]
    ):
        sc = Solution()
        assert (
            sc.queensAttacktheKing(
                queens,
                king,
            )
            == output
        )
