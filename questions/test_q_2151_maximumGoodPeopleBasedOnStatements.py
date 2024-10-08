import pytest
from q_2151_maximumGoodPeopleBasedOnStatements import Solution


@pytest.mark.parametrize(
    "statements, output",
    [([[2, 1, 2], [1, 2, 2], [2, 0, 2]], 2), ([[2, 0], [0, 2]], 1)],
)
class TestSolution:
    def test_maximumGood(self, statements: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maximumGood(
                statements,
            )
            == output
        )
