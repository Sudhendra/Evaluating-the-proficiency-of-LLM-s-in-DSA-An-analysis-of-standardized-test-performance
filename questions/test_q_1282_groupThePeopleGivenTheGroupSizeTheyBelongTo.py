import pytest
from q_1282_groupThePeopleGivenTheGroupSizeTheyBelongTo import Solution


@pytest.mark.parametrize(
    "groupSizes, output",
    [
        ([3, 3, 3, 3, 3, 1, 3], [[5], [0, 1, 2], [3, 4, 6]]),
        ([2, 1, 3, 3, 3, 2], [[1], [0, 5], [2, 3, 4]]),
    ],
)
class TestSolution:
    def test_groupThePeople(self, groupSizes: List[int], output: List[List[int]]):
        sc = Solution()
        assert (
            sc.groupThePeople(
                groupSizes,
            )
            == output
        )
