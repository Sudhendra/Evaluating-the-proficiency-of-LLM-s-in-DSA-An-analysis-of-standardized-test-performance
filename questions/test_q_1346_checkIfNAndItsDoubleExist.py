import pytest
from q_1346_checkIfNAndItsDoubleExist import Solution


@pytest.mark.parametrize("arr, output", [([10, 2, 5, 3], True), ([3, 1, 7, 11], False)])
class TestSolution:
    def test_checkIfExist(self, arr: List[int], output: bool):
        sc = Solution()
        assert (
            sc.checkIfExist(
                arr,
            )
            == output
        )
