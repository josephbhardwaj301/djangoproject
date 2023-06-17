#               .format method


my_name="Joseph"
print("1 Hello\n"+my_name)  #string interpolation

print('2 This is a string {}'.format('INSERTED'))
print('3 The {} {} {}'.format('fox','brown','quick'))
print('4 The {2} {1} {0}'.format('fox','brown','quick')) # This will apply word postion according to Index given in the curly braces
print('5 The {0} {0} {0}'.format('fox')) # This will print same word repeatedly
print('6 The {f} {b} {q}'.format(f='fox',b='brown',q='quick'))

#    Float formatting "{value:width.precision f}"
result=100/777
print(result)
print("1 The result was {}".format(result))
print("2 The result was {r}".format(r=result))
print("3 The result was {r:1.7f}".format(r=result))

#f format string

name="Jose"
print('Hello,his name is {}'.format(name))

name="Sam"
age=3
print(f'{name} is {age} years old.')