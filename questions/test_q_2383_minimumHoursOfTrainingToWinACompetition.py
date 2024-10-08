import pytest
from q_2383_minimumHoursOfTrainingToWinACompetition import Solution


@pytest.mark.parametrize(
    "initialEnergy, initialExperience, energy, experience, output",
    [(5, 3, [1, 4, 3, 2], [2, 6, 3, 1], 8), (2, 4, [1], [3], 0)],
)
class TestSolution:
    def test_minNumberOfHours(
        self,
        initialEnergy: int,
        initialExperience: int,
        energy: List[int],
        experience: List[int],
        output: int,
    ):
        sc = Solution()
        assert (
            sc.minNumberOfHours(
                initialEnergy,
                initialExperience,
                energy,
                experience,
            )
            == output
        )
