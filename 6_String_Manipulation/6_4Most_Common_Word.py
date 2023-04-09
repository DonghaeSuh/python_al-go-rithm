# My Way
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=re.sub('[^\w]',' ',paragraph).lower()
        words=[word for word in paragraph.split() if word not in banned]
        
        count=collections.Counter(words)
        return count.most_common(1)[0][0]
      
# collections'defaultdict() 사용
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=re.sub('[^\w]',' ',paragraph).lower()
        words=[word for word in paragraph.split() if word not in banned]
        
        count=collections.defaultdict(int) # defaultdict
        for word in words:
            count[word]+=1     
            # 'word' : 단어 / count['word'] = 'word'를 key로 가지는 요소의 value
        
        # value값이 가장 큰 key를 가져오기 위해 argmax같은 도구가 있다면 좋겠지만, max에 key를 지정해 argmax를 추출

        return max(count,key=count.get) # vlaue를 기준으로 max 판단
      
 
# dictionary .get() 
dictionary.get('key' , ‘해당 key가 존재하지 않을 경우 해당 key에 새롭게 할당할 value’) 
