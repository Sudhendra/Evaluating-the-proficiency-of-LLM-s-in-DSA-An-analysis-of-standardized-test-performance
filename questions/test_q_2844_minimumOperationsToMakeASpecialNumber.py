import pytest
from q_2844_minimumOperationsToMakeASpecialNumber import Solution


@pytest.mark.parametrize("num, output", [("2245047", 2), ("2908305", 3), ("10", 1)])
class TestSolution:
    def test_minimumOperations(self, num: str, output: int):
        sc = Solution()
        assert (
            sc.minimumOperations(
                num,
            )
            == output
        )
