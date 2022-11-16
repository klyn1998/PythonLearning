# def 函数名(参数)：
#   函数体
# 调用参数：函数名(参数)

# 函数声明时，括号里的参数称为形式参数，简称形参
# 形参的值是不确定的
def tell_story(person1, person2):
    print('从前有座山')
    print('山上有座庙')
    print('庙里有个' + person1)
    print('还有一个' + person2)
    print(person1 + '在给' + person2 + '讲故事')
    print('故事的内容是')


# 调用参数时传递数据
# 函数调用时传入的参数，才是真正参与运算的数据，称为实际参数，简称实参
tell_story('老道', '道童')  # 会把实参意义对应传递，交给形参处理
tell_story('师太', '小尼姑')

# 还可以通过定义变量名的形式给形参赋值
tell_story(person2='青年', person1='禅师')
