
def averaging_vectors (vector_1, vector_2):
	average = []
	for i in range(len(vector_1)):
		average.append((vector_1[i]+vector_2[i])/2)
	return average

