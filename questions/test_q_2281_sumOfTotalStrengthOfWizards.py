import pytest
from q_2281_sumOfTotalStrengthOfWizards import Solution


@pytest.mark.parametrize("strength, output", [([1, 3, 1, 2], 44), ([5, 4, 6], 213)])
class TestSolution:
    def test_totalStrength(self, strength: List[int], output: int):
        sc = Solution()
        assert (
            sc.totalStrength(
                strength,
            )
            == output
        )
