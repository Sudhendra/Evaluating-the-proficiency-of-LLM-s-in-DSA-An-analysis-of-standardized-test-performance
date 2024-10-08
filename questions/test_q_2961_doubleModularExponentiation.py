import pytest
from q_2961_doubleModularExponentiation import Solution


@pytest.mark.parametrize(
    "variables, target, output",
    [
        ([[2, 3, 3, 10], [3, 3, 3, 1], [6, 1, 1, 4]], 2, [0, 2]),
        ([[39, 3, 1000, 1000]], 17, []),
    ],
)
class TestSolution:
    def test_getGoodIndices(
        self, variables: List[List[int]], target: int, output: List[int]
    ):
        sc = Solution()
        assert (
            sc.getGoodIndices(
                variables,
                target,
            )
            == output
        )
