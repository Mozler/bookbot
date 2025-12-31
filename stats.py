def get_num_words(filepath):
	with open(filepath) as f:
		return len(f.read().split())

def count_chars(filepath):
	d = {}
	with open(filepath) as f:
		for c in f.read().lower():
			if c not in d: d[c] = 0
			d[c] += 1
	return d

def sort_by_count(filepath):
	d = count_chars(filepath)
	sorted_list = [{'char':char, 'count':count} for char, count in d.items()]
	sorted_list.sort(reverse=True, key=lambda item: item['count'])
	return sorted_list
