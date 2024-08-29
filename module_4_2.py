a = 10
def test_function():
    global b
    b = 15
    def inner_function():
        print('Я в области видимости функции test_function')
        print('a -', a, 'внутри test_function')
        print('b -', b, 'внутри test_function')
    #end of inner_function
    inner_function()

# end of test_function

test_function()
# inner_function()  при вызове получаю ошибку NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
print(a)
print('b -', b, 'основное пространство')