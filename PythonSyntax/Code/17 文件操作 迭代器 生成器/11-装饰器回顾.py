def can_play(fn):
    def inner(name, game, *args, **kwargs):
        if kwargs.get('clock', 23) >= 22:
            raise ValueError('太晚了')
        else:
            fn(name, game)

    return inner


@can_play
def play_game(name, game):
    print(name + '正在玩' + game)


# play_game('allen', 'dnf', clock=20)
