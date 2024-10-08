import pytest
from q_2251_numberOfFlowersInFullBloom import Solution


@pytest.mark.parametrize(
    "flowers, people, output",
    [
        ([[1, 6], [3, 7], [9, 12], [4, 13]], [2, 3, 7, 11], [1, 2, 2, 2]),
        ([[1, 10], [3, 3]], [3, 3, 2], [2, 2, 1]),
    ],
)
class TestSolution:
    def test_fullBloomFlowers(
        self, flowers: List[List[int]], people: List[int], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.fullBloomFlowers(
                flowers,
                people,
            )
            == output
        )
