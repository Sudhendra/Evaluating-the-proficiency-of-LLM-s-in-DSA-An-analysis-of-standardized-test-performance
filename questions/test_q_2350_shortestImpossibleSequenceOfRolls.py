import pytest
from q_2350_shortestImpossibleSequenceOfRolls import Solution


@pytest.mark.parametrize(
    "rolls, k, output",
    [
        ([4, 2, 1, 2, 3, 3, 2, 4, 1], 4, 3),
        ([1, 1, 2, 2], 2, 2),
        ([1, 1, 3, 2, 2, 2, 3, 3], 4, 1),
    ],
)
class TestSolution:
    def test_shortestSequence(self, rolls: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.shortestSequence(
                rolls,
                k,
            )
            == output
        )
