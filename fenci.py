# -*- coding: utf-8 -*-
import jieba

def stopwords():
    "停用词"
    stopwords_list = []
    with open('./corpus/stopwords.txt', 'rb') as fs:
        line = fs.readline()
        while line:
            word = line.strip()
            stopwords_list.append(str(word, encoding='utf-8'))
            line = fs.readline()
    fs.close()
    return stopwords_list

def check_chain_chinese(str):
    "判断词语是否是中文词"
    for ch in str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

def fenci():
    with open("./corpus/xiaoshuo.txt", 'rb') as fr, open("./corpus/wordlist.txt", 'w', encoding="utf-8") as fw:
        stopwords_list = stopwords()
        line = fr.readline()
        worldlist = []
        while line:
            sentece = line.strip()
            words = jieba.cut(str(sentece, encoding='utf-8'))
            for w in list(words):
                if w not in stopwords_list and check_chain_chinese(w) and len(list(w)) >= 2:
                    worldlist.append(w)
            line = fr.readline()
        print(len(worldlist))
        fw.write(' '.join(worldlist))

        fr.close()
        fw.close()
        return  worldlist

if __name__ == "__main__":

    fenci()
