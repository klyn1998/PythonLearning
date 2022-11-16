# 提需求/改需求
# 如果超过22点不让玩游戏；如果获取不到时间，默认不让玩
# 开放封闭原则
def can_play(fn):
    def inner(x, y, *args, **kwargs):
        # print(args)
        clock = kwargs.get('clock', 23)
        if clock > 22:
            print('太晚了')
        else:
            fn(x, y)

    return inner


@can_play
def play_game(name, game):
    print('{}正在玩{}'.format(name, game))


play_game('allen', 'dnf', clock=18)
play_game('bob', 'ow')
