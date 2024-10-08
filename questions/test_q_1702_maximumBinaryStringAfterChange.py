import pytest
from q_1702_maximumBinaryStringAfterChange import Solution


@pytest.mark.parametrize("binary, output", [("000110", "111011"), ("01", "01")])
class TestSolution:
    def test_maximumBinaryString(self, binary: str, output: str):
        sc = Solution()
        assert (
            sc.maximumBinaryString(
                binary,
            )
            == output
        )
