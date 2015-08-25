import copy


# input a list of lists [[e1,e2],[e3],[e4,e5]]
# output a list of all combinaitons [[e1,e3,e4],[e1,e3,e5],[e2,e3,e4],[e2,e3,e5]]
def allCombination(lsts):
	if len(lsts) == 1:
		return [[e] for e in lsts[0]]
	lsts = copy.deepcopy(lsts)
	cur = lsts.pop()

	output = []
	for e in cur:
		right = allCombination(lsts)
		right = [lst+[e] for lst in right]
		output += right
	return output


if __name__ == '__main__':
	print allCombination([[1,2],[3],[4,5]])