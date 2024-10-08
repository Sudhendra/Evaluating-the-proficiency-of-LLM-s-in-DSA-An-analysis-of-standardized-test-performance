import pytest
from q_1203_sortItemsByGroupsRespectingDependencies import Solution


@pytest.mark.parametrize(
    "n, m, group, beforeItems, output",
    [
        (
            8,
            2,
            [-1, -1, 1, 0, 0, 1, 0, -1],
            [[], [6], [5], [6], [3, 6], [], [], []],
            [6, 3, 4, 1, 5, 2, 0, 7],
        ),
        (8, 2, [-1, -1, 1, 0, 0, 1, 0, -1], [[], [6], [5], [6], [3], [], [4], []], []),
    ],
)
class TestSolution:
    def test_sortItems(
        self,
        n: int,
        m: int,
        group: List[int],
        beforeItems: List[List[int]],
        output: List[int],
    ):
        sc = Solution()
        assert (
            sc.sortItems(
                n,
                m,
                group,
                beforeItems,
            )
            == output
        )
