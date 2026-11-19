"""第 57 批：抽卡保底在跨卡池时提前触发：保底计数只存在本地缓..."""

def pity_key(pool_group, user_id):
    """返回保底键。"""
    raise NotImplementedError("TODO: pity_key")

def guarantee_on_ten(index):
    """判断十连第几抽触发保底。"""
    raise NotImplementedError("TODO: guarantee_on_ten")

def pity_reset(count, triggered):
    """触发后重置保底。"""
    raise NotImplementedError("TODO: pity_reset")

def inherit_pity(count, source_group, target_group):
    """跨卡池继承保底。"""
    raise NotImplementedError("TODO: inherit_pity")

def confirm_result(local, server):
    """以服务器结果为准。"""
    raise NotImplementedError("TODO: confirm_result")

def pity_after_batch(count, pulls, success):
    """批量抽卡后写回计数。"""
    raise NotImplementedError("TODO: pity_after_batch")

def target_record(target, count):
    """记录保底目标。"""
    raise NotImplementedError("TODO: target_record")

def hot_reload_migrate(count, old_rate, new_rate):
    """热更新迁移保底计数。"""
    raise NotImplementedError("TODO: hot_reload_migrate")

def public_rate(single_rate, ten_guarantee):
    """返回十连公示概率。"""
    raise NotImplementedError("TODO: public_rate")

def pool_group(pool_id, event_id):
    """返回卡池组键。"""
    raise NotImplementedError("TODO: pool_group")
