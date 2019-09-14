'hello' + "world"
'\"yes,\" I am.'
'\"yes\", we are.'
print('\"yes\", we are')
print('\"NO,\" we aren\'t')

>>> '\"yes,\" I am.'
'"yes," I am.'
>>> '\"yes\", we are.'
'"yes", we are.'
>>> print('\"yes\", we are')
"yes", we are
>>> print('\"NO,\" we aren\'t')
"NO," we aren't
>>> print('\'no,\' we aren\'t')
'no,' we aren't

>>> print('C:\some\name')
C:\some
ame
>>> print(r'C:\some\name')
C:\some\name

'hello' + ' ' + 'world'
('hello' + ' ' + 'world') * 3

>>> x = 'laptop'
>>> x[:]
'laptop'
>>> x[0:2]
'la'
>>> x[3:]
'top'
>>> x[:2]
'la'
>>> x = 'laptop'
>>> x[:]
'laptop'
>>> x[0:3]
'lap'
>>> x[3:]
'top'
>>> x[:3]
'lap'
>>> x[1]
'a'
>>> x[:3] + x[3:]
'laptop'
>>>
>>> x[-1]
'p'
>>> x[:7]
'laptop'

>>> len(x)
6
>>> len(x[0:3]) + 4
7
>>> 'string' + str(21)
'string21'
>>> 23 + int('2')
25

#string are immutable
>>> x[1:3] + 'p' 
'app'

>>> x = [2, 4, 6, 8, 10]
>>> y = [1, 3, 5, 7, 9]
>>> x + y
[2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
>>> print(x + y)
[2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
>>> print(x,y)
[2, 4, 6, 8, 10] [1, 3, 5, 7, 9]
>>> print([x,y])
[[2, 4, 6, 8, 10], [1, 3, 5, 7, 9]]
>>> x[0] = 5
>>> x
[5, 4, 6, 8, 10]

>>> a = [1, 2, 3, 4, 5]
>>> b = [6, 7, 8, 9, 10]
>>> c = ['l', 'o', 's', 't']
>>> x = [a, b, c]
>>> x
[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], ['l', 'o', 's', 't']]
>>> x[2][3] = 'e'
>>> x
[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], ['l', 'o', 's', 'e']]