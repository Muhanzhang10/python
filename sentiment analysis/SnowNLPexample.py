from snownlp import SnowNLP
from snownlp import sentiment


#example1 (sentiment analysis)
'''
a = "我爱工作。"
s = SnowNLP(a)
sent = s.sentences
for sen in sent:
    s = SnowNLP(sen)
    print(s.sentences)
    print(s.sentiments)
'''

sentence = '关于这个问题，我只能说“无可奉告”，我什么也不说呢，你们就不高兴了。你一定要我说点什么。你们哪，图样图森破，就一一个好'
sequence = sentence.split('。')
for i in range(len(sequence)):
    temp = SnowNLP(sequence[i])
    print(sequence[i])
    print(temp.sentiments)



#example2 (summary)
'''
a = "关于这个问题，我只能说“无可奉告”，我什么也不说呢，你们就不高兴了。你一定要我说点什么。你们哪，图样图森破，就一一个好"
s = SnowNLP(a)
print(s.summary(2))
'''