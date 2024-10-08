import pytest
from q_2433_findTheOriginalArrayOfPrefixXor import Solution


@pytest.mark.parametrize(
    "pref, output", [([5, 2, 0, 3, 1], [5, 7, 2, 3, 2]), ([13], [13])]
)
class TestSolution:
    def test_findArray(self, pref: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.findArray(
                pref,
            )
            == output
        )
