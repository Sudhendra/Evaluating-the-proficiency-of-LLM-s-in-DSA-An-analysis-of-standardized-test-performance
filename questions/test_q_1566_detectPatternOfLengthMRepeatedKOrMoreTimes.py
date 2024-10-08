import pytest
from q_1566_detectPatternOfLengthMRepeatedKOrMoreTimes import Solution


@pytest.mark.parametrize(
    "arr, m, k, output",
    [
        ([1, 2, 4, 4, 4, 4], 1, 3, True),
        ([1, 2, 1, 2, 1, 1, 1, 3], 2, 2, True),
        ([1, 2, 1, 2, 1, 3], 2, 3, False),
    ],
)
class TestSolution:
    def test_containsPattern(self, arr: List[int], m: int, k: int, output: bool):
        sc = Solution()
        assert (
            sc.containsPattern(
                arr,
                m,
                k,
            )
            == output
        )
