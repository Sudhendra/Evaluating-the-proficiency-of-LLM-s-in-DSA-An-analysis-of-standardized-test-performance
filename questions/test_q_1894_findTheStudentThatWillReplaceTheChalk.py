import pytest
from q_1894_findTheStudentThatWillReplaceTheChalk import Solution


@pytest.mark.parametrize(
    "chalk, k, output", [([5, 1, 5], 22, 0), ([3, 4, 1, 2], 25, 1)]
)
class TestSolution:
    def test_chalkReplacer(self, chalk: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.chalkReplacer(
                chalk,
                k,
            )
            == output
        )
