import pytest
from q_0839_similarStringGroups import Solution


@pytest.mark.parametrize(
    "strs, output", [(["tars", "rats", "arts", "star"], 2), (["omv", "ovm"], 1)]
)
class TestSolution:
    def test_numSimilarGroups(self, strs: List[str], output: int):
        sc = Solution()
        assert (
            sc.numSimilarGroups(
                strs,
            )
            == output
        )
