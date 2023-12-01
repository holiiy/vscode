def arg_func(sex):
    def func1(b_func):
        def func2():
            if sex =='man':
                print('你不可以生娃')
            else:
                print('可以')
            return b_func()
        return func2
    return func1




@arg_func(sex='man')
def man():
    print('好好上班')

@arg_func(sex='woman')
def woman():
    print('好好学习')

man()
woman()