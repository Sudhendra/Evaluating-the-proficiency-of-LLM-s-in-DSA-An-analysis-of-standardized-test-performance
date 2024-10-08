import pytest
from q_1238_circularPermutationInBinaryRepresentation import Solution


@pytest.mark.parametrize(
    "n, start, output", [(2, 3, [3, 2, 0, 1]), (3, 2, [2, 6, 7, 5, 4, 0, 1, 3])]
)
class TestSolution:
    def test_circularPermutation(self, n: int, start: int, output: List[int]):
        sc = Solution()
        assert (
            sc.circularPermutation(
                n,
                start,
            )
            == output
        )
