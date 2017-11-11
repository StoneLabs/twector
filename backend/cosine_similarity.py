import math


def cosine_similarity (vectore_x, vektore_y ):
	sum_xy, sum_xx,  sum_yy = 0, 0, 0
	for i in range(len(vectore_x)):
		x = vectore_1[i]; y = vectore_2[i]
		sum_xx += x*x
		sum_xy += x*y
		sum_yy += y*y
	return sum_xy/math.sqrt(sum_xx*sum_yy)

vectore_1, vectore_2 = [ 5, 0, 3, 0, 2, 0, 0, 2, 0, 0],, [ ,3, 0, 2, 0, 1, 1, 0, 1, 0, 1]
print(vectore_1, vectore_2, cosine_similarity(vectore_1, vectore_2))
