import pytest
from q_2136_earliestPossibleDayOfFullBloom import Solution


@pytest.mark.parametrize(
    "plantTime, growTime, output",
    [([1, 4, 3], [2, 3, 1], 9), ([1, 2, 3, 2], [2, 1, 2, 1], 9), ([1], [1], 2)],
)
class TestSolution:
    def test_earliestFullBloom(
        self, plantTime: List[int], growTime: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.earliestFullBloom(
                plantTime,
                growTime,
            )
            == output
        )
