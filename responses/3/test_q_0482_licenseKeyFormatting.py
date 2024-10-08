import pytest
from q_0482_licenseKeyFormatting import Solution


@pytest.mark.parametrize(
    "s, k, output", [("5F3Z-2e-9-w", 4, "5F3Z-2E9W"), ("2-5g-3-J", 2, "2-5G-3J")]
)
class TestSolution:
    def test_licenseKeyFormatting(self, s: str, k: int, output: str):
        sc = Solution()
        assert (
            sc.licenseKeyFormatting(
                s,
                k,
            )
            == output
        )
