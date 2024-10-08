import pytest
from q_2299_strongPasswordCheckerIi import Solution


@pytest.mark.parametrize(
    "password, output",
    [("IloveLe3tcode!", True), ("Me+You--IsMyDream", False), ("1aB!", False)],
)
class TestSolution:
    def test_strongPasswordCheckerII(self, password: str, output: bool):
        sc = Solution()
        assert (
            sc.strongPasswordCheckerII(
                password,
            )
            == output
        )
