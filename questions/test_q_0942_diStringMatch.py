import pytest
from q_0942_diStringMatch import Solution


@pytest.mark.parametrize(
    "s, output",
    [("IDID", [0, 4, 1, 3, 2]), ("III", [0, 1, 2, 3]), ("DDI", [3, 2, 0, 1])],
)
class TestSolution:
    def test_diStringMatch(self, s: str, output: List[int]):
        sc = Solution()
        assert (
            sc.diStringMatch(
                s,
            )
            == output
        )
