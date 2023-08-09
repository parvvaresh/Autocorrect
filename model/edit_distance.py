import numpy as np

class edit_distance:
	def __init__(self):
		pass

	def get_score(self, writer, ref):
		costs = np.zeros((len(writer) + 1, len(ref) + 1))
		backtrace = [[10 for _ in range(len(ref) + 1)] for _ in range(len(writer) + 1)]
		"""
		 0 --> insert
		 1 --> delete
		 2 --> alternative
		 3 --> same
		"""

		costs[0, : ] = [j for j in range(len(ref) + 1)]
		backtrace[0][ : ] = [0 for j in range(len(ref) + 1)]

		costs[ : , 0] = [j for j in range(len(writer) + 1)]
		backtrace[ : ][0] = [1 for j in range(len(writer) + 1)]

		for index_write in range(1 , len(writer) + 1):
			for index_ref in range(1, len(ref) + 1):
				if ref[index_ref - 1] == writer[index_write - 1]:
					costs[index_write][index_ref] = costs[index_write - 1][index_ref - 1]
					backtrace[index_write][index_ref] = 3

				else:
					delete = costs[index_write - 1][index_ref]
					insert = costs[index_write][index_ref - 1]
					alternative = costs[index_write - 1][index_ref - 1]
					fainal = min(delete, insert, alternative)
					costs[index_write][index_ref] = fainal + 1

					if fainal == delete:
						backtrace[index_write][index_ref] = 1
					if fainal == insert:
						backtrace[index_write][index_ref] = 0
					if fainal == alternative:
						backtrace[index_write][index_ref] = 2


		index_write, index_ref = len(writer), len(ref)
		self.num_same_char = 0
		self.num_insert = 0
		self.num_delete = 0
		self.num_alternative = 0
		while index_write > 0 or index_ref > 0:
			if backtrace[index_write][index_ref] == 3:
				self.num_same_char += 1
				index_write -= 1
				index_ref -= 1

			elif backtrace[index_write][index_ref] == 2:
				self.num_alternative += 1
				index_write -= 1
				index_ref -= 1

			elif backtrace[index_write][index_ref] == 1:
				self.num_delete += 1
				index_write -= 1

			elif backtrace[index_write][index_ref] == 0:
				self.num_insert += 1
				index_ref -= 1	

		score = (self.num_delete + self.num_insert + self.num_alternative) / len(ref)
		return score





	def get_details(self):
		return {
			"same char" : self.num_same_char,
			"number of delete" : self.num_delete,
			"number of insert" : self.num_insert,
			"number of alternative" : self.num_alternative
		}



