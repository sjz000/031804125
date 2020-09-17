import unittest
import compute_similarity

class Test(unittest.TestCase):

	def test_add(self):
		with open(r"E:\python\软工实践\第一次编程作业\orig.txt", "r", encoding='UTF-8') as fp:
			orig_text = fp.read()
		with open(r"E:\python\软工实践\第一次编程作业\orig_0.8_add.txt", "r", encoding='UTF-8') as fp:
			copy_text = fp.read()
		similarity = compute_similarity.Similarity(orig_text, copy_text, int(len(orig_text)*0.15))
		similarity = round(similarity.similar(), 2)
		print("orig_0.8_add.txt 与 orig.txt的相似度:" + " " + str(similarity))

	def test_del(self):
		with open(r"E:\python\软工实践\第一次编程作业\orig.txt", "r", encoding='UTF-8') as fp:
			orig_text = fp.read()
		with open(r"E:\python\软工实践\第一次编程作业\orig_0.8_del.txt", "r", encoding='UTF-8') as fp:
			copy_text = fp.read()
		similarity = compute_similarity.Similarity(orig_text, copy_text, int(len(orig_text)*0.15))
		similarity = round(similarity.similar(), 2)
		print("orig_0.8_del.txt 与 orig.txt的相似度:" + " " + str(similarity))
		
	def test_dis_1(self):
		with open(r"E:\python\软工实践\第一次编程作业\orig.txt", "r", encoding='UTF-8') as fp:
			orig_text = fp.read()
		with open(r"E:\python\软工实践\第一次编程作业\orig_0.8_dis_1.txt", "r", encoding='UTF-8') as fp:
			copy_text = fp.read()
		similarity = compute_similarity.Similarity(orig_text, copy_text, int(len(orig_text)*0.15))
		similarity = round(similarity.similar(), 2)
		print("orig_0.8_dis_1.txt 与 orig.txt的相似度:" + " " + str(similarity))
		
	def test_dis_3(self):
		with open(r"E:\python\软工实践\第一次编程作业\orig.txt", "r", encoding='UTF-8') as fp:
			orig_text = fp.read()
		with open(r"E:\python\软工实践\第一次编程作业\orig_0.8_dis_3.txt", "r", encoding='UTF-8') as fp:
			copy_text = fp.read()
		similarity = compute_similarity.Similarity(orig_text, copy_text, int(len(orig_text)*0.15))
		similarity = round(similarity.similar(), 2)
		print("orig_0.8_dis_3.txt 与 orig.txt的相似度:" + " " + str(similarity))
		
	def test_dis_7(self):
		with open(r"E:\python\软工实践\第一次编程作业\orig.txt", "r", encoding='UTF-8') as fp:
			orig_text = fp.read()
		with open(r"E:\python\软工实践\第一次编程作业\orig_0.8_dis_7.txt", "r", encoding='UTF-8') as fp:
			copy_text = fp.read()
		similarity = compute_similarity.Similarity(orig_text, copy_text, int(len(orig_text)*0.15))
		similarity = round(similarity.similar(), 2)
		print("orig_0.8_dis_7.txt 与 orig.txt的相似度:" + " " + str(similarity))
		
	def test_dis_10(self):
		with open(r"E:\python\软工实践\第一次编程作业\orig.txt", "r", encoding='UTF-8') as fp:
			orig_text = fp.read()
		with open(r"E:\python\软工实践\第一次编程作业\orig_0.8_dis_10.txt", "r", encoding='UTF-8') as fp:
			copy_text = fp.read()
		similarity = compute_similarity.Similarity(orig_text, copy_text, int(len(orig_text)*0.15))
		similarity = round(similarity.similar(), 2)
		print("orig_0.8_dis_10.txt 与 orig.txt的相似度:" + " " + str(similarity))
		
	def test_dis_15(self):
		with open(r"E:\python\软工实践\第一次编程作业\orig.txt", "r", encoding='UTF-8') as fp:
			orig_text = fp.read()
		with open(r"E:\python\软工实践\第一次编程作业\orig_0.8_dis_15.txt", "r", encoding='UTF-8') as fp:
			copy_text = fp.read()
		similarity = compute_similarity.Similarity(orig_text, copy_text, int(len(orig_text)*0.15))
		similarity = round(similarity.similar(), 2)
		print("orig_0.8_dis_15.txt 与 orig.txt的相似度:" + " " + str(similarity))
		
	def test_mix(self):
		with open(r"E:\python\软工实践\第一次编程作业\orig.txt", "r", encoding='UTF-8') as fp:
			orig_text = fp.read()
		with open(r"E:\python\软工实践\第一次编程作业\orig_0.8_mix.txt", "r", encoding='UTF-8') as fp:
			copy_text = fp.read()
		similarity = compute_similarity.Similarity(orig_text, copy_text, int(len(orig_text)*0.15))
		similarity = round(similarity.similar(), 2)
		print("orig_0.8_mix.txt 与 orig.txt的相似度:" + " " + str(similarity))
		
	def test_rep(self):
		with open(r"E:\python\软工实践\第一次编程作业\orig.txt", "r", encoding='UTF-8') as fp:
			orig_text = fp.read()
		with open(r"E:\python\软工实践\第一次编程作业\orig_0.8_rep.txt", "r", encoding='UTF-8') as fp:
			copy_text = fp.read()
		similarity = compute_similarity.Similarity(orig_text, copy_text, int(len(orig_text)*0.15))
		similarity = round(similarity.similar(), 2)
		print("orig_0.8_rep.txt 与 orig.txt的相似度:" + " " + str(similarity))

if __name__ == '__main__':
	
	unittest.main()
# 031804125
