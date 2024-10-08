import pytest
from q_1780_checkIfNumberIsASumOfPowersOfThree import Solution


@pytest.mark.parametrize("n, output", [(12, True), (91, True), (21, False)])
class TestSolution:
    def test_checkPowersOfThree(self, n: int, output: bool):
        sc = Solution()
        assert (
            sc.checkPowersOfThree(
                n,
            )
            == output
        )
