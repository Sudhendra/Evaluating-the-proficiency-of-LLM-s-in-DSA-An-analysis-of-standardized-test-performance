import pytest
from q_1345_jumpGameIv import Solution


@pytest.mark.parametrize(
    "arr, output",
    [
        ([100, -23, -23, 404, 100, 23, 23, 23, 3, 404], 3),
        ([7], 0),
        ([7, 6, 9, 6, 9, 6, 9, 7], 1),
    ],
)
class TestSolution:
    def test_minJumps(self, arr: List[int], output: int):
        sc = Solution()
        assert (
            sc.minJumps(
                arr,
            )
            == output
        )
