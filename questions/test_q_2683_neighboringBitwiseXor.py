import pytest
from q_2683_neighboringBitwiseXor import Solution


@pytest.mark.parametrize(
    "derived, output", [([1, 1, 0], True), ([1, 1], True), ([1, 0], False)]
)
class TestSolution:
    def test_doesValidArrayExist(self, derived: List[int], output: bool):
        sc = Solution()
        assert (
            sc.doesValidArrayExist(
                derived,
            )
            == output
        )
