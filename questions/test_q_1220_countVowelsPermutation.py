import pytest
from q_1220_countVowelsPermutation import Solution


@pytest.mark.parametrize("n, output", [(1, 5), (2, 10), (5, 68)])
class TestSolution:
    def test_countVowelPermutation(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.countVowelPermutation(
                n,
            )
            == output
        )
