import pytest
from q_2358_maximumNumberOfGroupsEnteringACompetition import Solution


@pytest.mark.parametrize("grades, output", [([10, 6, 12, 7, 3, 5], 3), ([8, 8], 1)])
class TestSolution:
    def test_maximumGroups(self, grades: List[int], output: int):
        sc = Solution()
        assert (
            sc.maximumGroups(
                grades,
            )
            == output
        )
