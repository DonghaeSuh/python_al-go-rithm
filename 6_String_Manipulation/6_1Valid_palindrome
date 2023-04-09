# 리스트로 변환
class Solution:

  def isPalindrome(self, s: str) -> bool:
    str = []
    for char in s:
      if char.isalnum():
        str.append(char.lower())
    while len(str) > 1:
      if str.pop(0) != str.pop():
        return False
    return True


# 데크 자료형 이용 최적화
class Solution:

  def isPalindrome(self, s: str) -> bool:
    str = []
    for char in s:
      if char.isalnum():
        str.append(char.lower())
    while len(str) > 1:
      if str.pop(0) != str.pop():
        return False
    return True


# 슬라이싱 사용
class Solution:

  def isPalindrome(self, s: str) -> bool:
    s = s.lower()

    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]
