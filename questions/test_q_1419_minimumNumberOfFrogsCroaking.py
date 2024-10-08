import pytest
from q_1419_minimumNumberOfFrogsCroaking import Solution


@pytest.mark.parametrize(
    "croakOfFrogs, output", [("croakcroak", 1), ("crcoakroak", 2), ("croakcrook", -1)]
)
class TestSolution:
    def test_minNumberOfFrogs(self, croakOfFrogs: str, output: int):
        sc = Solution()
        assert (
            sc.minNumberOfFrogs(
                croakOfFrogs,
            )
            == output
        )
