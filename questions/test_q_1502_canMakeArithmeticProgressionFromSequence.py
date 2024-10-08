import pytest
from q_1502_canMakeArithmeticProgressionFromSequence import Solution


@pytest.mark.parametrize("arr, output", [([3, 5, 1], True), ([1, 2, 4], False)])
class TestSolution:
    def test_canMakeArithmeticProgression(self, arr: List[int], output: bool):
        sc = Solution()
        assert (
            sc.canMakeArithmeticProgression(
                arr,
            )
            == output
        )
