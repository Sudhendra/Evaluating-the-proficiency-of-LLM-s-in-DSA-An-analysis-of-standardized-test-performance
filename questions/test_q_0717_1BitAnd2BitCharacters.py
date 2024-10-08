import pytest
from q_0717_1BitAnd2BitCharacters import Solution


@pytest.mark.parametrize("bits, output", [([1, 0, 0], True), ([1, 1, 1, 0], False)])
class TestSolution:
    def test_isOneBitCharacter(self, bits: List[int], output: bool):
        sc = Solution()
        assert (
            sc.isOneBitCharacter(
                bits,
            )
            == output
        )
