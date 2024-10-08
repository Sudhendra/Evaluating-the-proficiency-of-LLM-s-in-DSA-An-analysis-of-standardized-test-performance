import pytest
from q_1641_countSortedVowelStrings import Solution


@pytest.mark.parametrize("n, output", [(1, 5), (2, 15), (33, 66045)])
class TestSolution:
    def test_countVowelStrings(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.countVowelStrings(
                n,
            )
            == output
        )
