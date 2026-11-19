import pytest
from gameplay import gacha_pity as mod

CASES = [
    ("key_pair", 'm.pity_key("limited", 7) == ("limited", 7)'),
    ("ten_true", 'm.guarantee_on_ten(10) is True'),
    ("ten_false", 'm.guarantee_on_ten(5) is False'),
    ("reset_true", 'm.pity_reset(9, True) == 0'),
    ("reset_false", 'm.pity_reset(9, False) == 9'),
    ("inherit_same", 'm.inherit_pity(5, "a", "a") == 5'),
    ("inherit_diff", 'm.inherit_pity(5, "a", "b") == 0'),
    ("confirm_server", 'm.confirm_result(3, 5) == 5'),
    ("batch_success", 'm.pity_after_batch(4, 10, True) == 14'),
    ("batch_fail", 'm.pity_after_batch(4, 10, False) == 4'),
    ("target_pair", 'm.target_record("up", 3) == ("up", 3)'),
    ("hot_migrate", 'm.hot_reload_migrate(10, 0.1, 0.2) == 5'),
    ("public_ten", 'm.public_rate(0.01, 0.1) == approx(0.2)'),
    ("group_key", 'm.pool_group("p1", "e1") == "p1:e1"'),
    ("ten_zero", 'm.guarantee_on_ten(0) is False')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
