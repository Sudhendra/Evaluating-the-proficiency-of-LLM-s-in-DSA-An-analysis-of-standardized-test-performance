import pytest
from q_1585_checkIfStringIsTransformableWithSubstringSortOperations import Solution


@pytest.mark.parametrize(
    "s, t, output",
    [("84532", "34852", True), ("34521", "23415", True), ("12345", "12435", False)],
)
class TestSolution:
    def test_isTransformable(self, s: str, t: str, output: bool):
        sc = Solution()
        assert (
            sc.isTransformable(
                s,
                t,
            )
            == output
        )
