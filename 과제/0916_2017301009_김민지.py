Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> test_list = ['one','two','three']
>>> for i in test_list:
	x = i+'!'
	print(x)

	
one!
two!
three!
>>> number = 0
>>> for score in [90,25,67,45,93]:
	number+=i
	if score>=60:
		print("%d번 학생은 합격입니다",%number)
		
SyntaxError: invalid syntax
>>> for score in [90,25,67,45,93]:
	number+=i
	if score>=60:
		print("%d번 학생은 합격입니다"%number)
	else:
		print("%d번 학생은 불합격입니다."%number)

		
Traceback (most recent call last):
  File "<pyshell#14>", line 2, in <module>
    number+=i
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
>>> for score in [90,25,67,45,93]:
	number+=1
	if score>=60:
		print("%d번 학생은 합격입니다"%number)
	else:
		print("%d번 학생은 불합격입니다."%number)

		
1번 학생은 합격입니다
2번 학생은 불합격입니다.
3번 학생은 합격입니다
4번 학생은 불합격입니다.
5번 학생은 합격입니다
>>> def sum1(a,b):
	x=a+b
	return x

>>> def sum2(*args):
	x=0
	for i in args:
		x+=i
	return x

>>> a=5
>>> b=3
>>> sum1(a,b)
8
>>> sum1(3,5)
8
>>> sum2(1,2,3,4,5)
15
>>> sum2(2,3.5,10)
15.5
>>> str = '20201231Thursday'
>>> year=str[0:4]
>>> year
'2020'
>>> mmdd=str[4:8]
>>> mmdd
'1231'
>>> day = str[8:]
>>> day
'Thursday'
>>>  a = ['쓰','레','기','통']
 
SyntaxError: unexpected indent
>>> a = ['쓰','레','기','통']
>>> a.reverse()
>>> a
['통', '기', '레', '쓰']
>>> dic = {"year":2020,"mm":12,"dd":31,"day":"Thursday","weather":"snow"}
>>> dic.keys()
dict_keys(['year', 'mm', 'dd', 'day', 'weather'])
>>> dic.values()
dict_values([2020, 12, 31, 'Thursday', 'snow'])
>>> line = 5
>>> for i in range(1,line+1):
	for j in range(i):
		print("*",end="")
	print()

	
*
**
***
****
*****
>>> import sys
>>> def avg(*args):
    myList=[]
    for i in args:
        myList.append(i)
    result = sum(myList)/len(args)
    print(result)

    
>>> avg(5,3,12,9)
7.25
>>> avg(2.4,3.2,7.3)
4.3
>>> avg(10,5)
7.5
>>> 