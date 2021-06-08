from snownlp import SnowNLP
from snownlp import sentiment


#example1 (sentiment analysis)
a = "我是真的服了。"
s = SnowNLP(a)
sent = s.sentences
for sen in sent:
    s = SnowNLP(sen)
    print(s.sentences)
    print(s.sentiments)



#example2 (summary)
a = "渣男老了，就会变成“渣大叔”。有些大叔爱的套路，藏得比海还深，你根本要不起。在这个满屏都在嫌弃“中年油腻”、“满脸褶子”、“爹味儿”的时代里，老少配爱情剧依旧不知疲倦地出现在大众视野。日前，由年过50的陈建斌与90后小花李一桐合作出演的都市爱情剧《爱我就别想太多》，受到网友铺天盖地的吐槽。陈建斌疏于对外貌的管理，腆着啤酒肚的他同女主站在一起，视觉年龄差比真实年龄差更大。"
s = SnowNLP(a)
print(s.summary(3))
