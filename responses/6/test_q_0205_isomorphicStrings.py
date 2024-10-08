import pytest
from q_0205_isomorphicStrings import Solution


@pytest.mark.parametrize(
    "s, t, output",
    [("egg", "add", True), ("foo", "bar", False), ("paper", "title", True)],
)
class TestSolution:
    def test_isIsomorphic(self, s: str, t: str, output: bool):
        sc = Solution()
        assert (
            sc.isIsomorphic(
                s,
                t,
            )
            == output
        )
