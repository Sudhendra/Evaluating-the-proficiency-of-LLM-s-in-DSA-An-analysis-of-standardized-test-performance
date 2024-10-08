import pytest
from q_0926_flipStringToMonotoneIncreasing import Solution


@pytest.mark.parametrize("s, output", [("00110", 1), ("010110", 2), ("00011000", 2)])
class TestSolution:
    def test_minFlipsMonoIncr(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.minFlipsMonoIncr(
                s,
            )
            == output
        )
