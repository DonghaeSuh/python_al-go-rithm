# 람다와 + 연산자 이용


class Solution:

  def reorderLogFiles(self, logs: List[str]) -> List[str]:

    # 식별자 바로 뒤에 있는 값이 문자인지 숫자인지 확인하여 분류
    letter, digit = [], []
    for log in logs:
      if log.split()[1].isdigit():
        digit.append(log)
      else:
        letter.append(log)

    # letter.sort(key=lambda s : (s.split()[1:],s.split()[0]))
    letter = sorted(letter, key=lambda s: (s.split()[1:], s.split()[0]))
    return letter + digit


# sort() & sorted() 테스트

# 문자열 sorted()
'''
b='zbdaf'
sorted(b)
['a','b','d','f','z']
'''

# 각 리스트 요소에 대해 소문자 변환 후 정렬
'''
sorted("This is a test string from Andrew".split(), key=str.lower) 
# 각 리스트 요소에 대해 호출
['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
'''

# 각 요소의 2번째 index를 기준으로 정렬
'''
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
'''

# 각 요소의 길이를 기준으로 정렬
'''
c= ['ccc','aaaa','d','bb']
sorted(c,key=len)
['d','bb','ccc','aaaa']
'''

# key 없이 sort()
'''
a = ['2 A', '1 B', '4 C', '1 A']
print(sorted(a))


def func(x):
  return (x.split()[1], x.split()[0])


print(sorted(a, key=func))

a = ['AC 2', 'BD 1', 'CA 4', 'AA 1']
print(sorted(a))

a = ['A D', 'B A', 'C C', 'A B']
print(sorted(a))
'''

# 문자열 key 사용 sorted()
'''
a=['cde','cfc','abc']

def fn(s):
    return s[0],s[-1]

print(sorted(a,key=fn))

['abc','cfc','cde']


a=['cde','cfc','abc']

print(sorted(a,key=lambda s : (s[0],s[-1]))

['abc','cfc','cde']
'''
