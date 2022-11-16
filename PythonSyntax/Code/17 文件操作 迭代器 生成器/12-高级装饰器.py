def can_play(clock):
    print('最外层函数被调用了，clock = {}'.format(clock))

    def handle_action(fn):
        print('handle_action被调用了，fn = {}'.format(fn))

        def do_action(name, game):
            if clock < 22:
                fn(name, game)
            else:
                print('太晚了')

        return do_action

    return handle_action


@can_play(21)  # 装饰器函数带参数
def play_game(name, game):
    print(name + '正在玩' + game)


play_game('allen', 'dnf')
