import pytest
from q_0385_miniParser import Solution


@pytest.mark.parametrize(
    "s, output", [("324", 324), ("[123,[456,[789]]]", [123, [456, [789]]])]
)
class TestSolution:
    def test_deserialize(self, s: str, output: NestedInteger):
        sc = Solution()
        assert (
            sc.deserialize(
                s,
            )
            == output
        )
