import pytest
from q_0393_utf8Validation import Solution


@pytest.mark.parametrize(
    "data, output", [([197, 130, 1], True), ([235, 140, 4], False)]
)
class TestSolution:
    def test_validUtf8(self, data: List[int], output: bool):
        sc = Solution()
        assert (
            sc.validUtf8(
                data,
            )
            == output
        )
