from stats import get_num_words, count_chars, sort_by_count
import sys

def main():
	if len(sys.argv) < 2:
		print('Usage: python3 main.py <path_to_book>')
		sys.exit(1)
	book_path = sys.argv[1]
	print(f'============ BOOKBOT ============')
	print(f'Analyzing book found at {book_path}...')
	print(f'----------- Word Count ----------')
	word_count = get_num_words(book_path)
	print(f'Found {word_count} total words')

	print(f'--------- Character Count -------')
	sorted_list = sort_by_count(book_path)
	for item in sorted_list:
		if not item['char'].isalpha(): continue
		print(f'{item['char']}: {item['count']}')
	print(f'============= END ===============')
	
main()
