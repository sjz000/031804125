import jieba
import jieba.analyse
from math import sqrt
import sys
from functools import reduce
class Similarity():
	def __init__(self,file1,file2,topK):
		self.file1 = file1
		self.file2 = file2
		self.topK = topK
	
	def keywords(self):
		#根据权重获取权重最高的K个关键词
		words = [i for i in jieba.lcut(self.file1, cut_all=True)]
		self.keywords1 = jieba.analyse.extract_tags(" ".join(words), topK=self.topK, withWeight=False)
		words = [i for i in jieba.lcut(self.file2, cut_all=True)]
		self.keywords2 = jieba.analyse.extract_tags(" ".join(words), topK=self.topK, withWeight=False)

	def mix_dicts(self):
		#将两篇文章的关键词合并，并且根据合并后的关键词建立字典
		union = set(self.keywords1).union(set(self.keywords2))
		self.dicts = {}
		i = 0
		for word in union:
			self.dicts[word] = i
			i += 1
		self.length = len(union)

	def list_codes(self):
		#将关键词转换为出现在字典中的位置
		self.codes1 = []
		for word in self.keywords1:
			self.codes1.append(self.dicts[word])
		self.codes2 = []
		for word in self.keywords2:
			self.codes2.append(self.dicts[word])

	def oneHot(self):
		self.listoneHot1 = [0]*self.length
		for i in self.codes1:
			self.listoneHot1[i] += 1
		self.listoneHot2 = [0]*self.length
		for i in self.codes2:
			self.listoneHot2[i] += 1

	def similar(self):
		#删除标点符号以及部分语气助词
		strs=[' ','\n','“','，','。','《','》','：','”','、','的','了','是','说','呀','啦','啊']
		for j in strs:
			self.file1=self.file1.replace(j,'')
			self.file2=self.file2.replace(j,'')
		#获取两篇文章的关键词以及分词结果
		self.keywords()
		#建立关键词字典
		self.mix_dicts()
		#将分词结果转换为出现在字典中的位置
		self.list_codes()
		#进行oneHot编码
		self.oneHot()
		#余弦相似度计算
		sum_ = 0
		for i in range(0,self.length):
			sum_ += self.listoneHot1[i] * self.listoneHot2[i]
		A = sqrt(reduce(lambda x,y: x+y, map(lambda x: x*x, self.listoneHot1)))
		B = sqrt(reduce(lambda x,y: x+y, map(lambda x: x*x, self.listoneHot2)))
		try:
			result = sum_/(A*B)
			return result
		except Exception as e:
			print(e)
			return 0.0
	
if __name__ == '__main__':
	oriPath = sys.argv[1]
	copyPath = sys.argv[2]
	ansPath = sys.argv[3]
	try:
		with open(oriPath,encoding='UTF-8') as fp:
			file1 = fp.read()
			words = [i for i in jieba.lcut(file1, cut_all=True) if i != '']
		with open(copyPath,encoding='UTF-8') as fp:
			file2 = fp.read()
		topK = int(len(words)*0.15)
	except:
		print("路径错误")
	s = Similarity(file1,file2,topK)
	similarity = round(s.similar(), 2)
	try:
		with open(ansPath, "w+", encoding='UTF-8') as fp:
			fp.write(str(similarity))
	except:
		print("路径错误")
# 031804125
