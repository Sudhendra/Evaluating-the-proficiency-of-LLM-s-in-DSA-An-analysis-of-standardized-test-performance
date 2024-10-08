import pytest
from q_0060_permutationSequence import Solution


@pytest.mark.parametrize("n, k, output", [(3, 3, "213"), (4, 9, "2314"), (3, 1, "123")])
class TestSolution:
    def test_getPermutation(self, n: int, k: int, output: str):
        sc = Solution()
        assert (
            sc.getPermutation(
                n,
                k,
            )
            == output
        )
