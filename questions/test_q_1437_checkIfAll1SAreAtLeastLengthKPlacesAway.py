import pytest
from q_1437_checkIfAll1SAreAtLeastLengthKPlacesAway import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [([1, 0, 0, 0, 1, 0, 0, 1], 2, True), ([1, 0, 0, 1, 0, 1], 2, False)],
)
class TestSolution:
    def test_kLengthApart(self, nums: List[int], k: int, output: bool):
        sc = Solution()
        assert (
            sc.kLengthApart(
                nums,
                k,
            )
            == output
        )
