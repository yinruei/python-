a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list(map(lambda x: x ** 2, a))
# print(squares)

even_squares = [x**2 for x in a if x % 2 == 0]
# print(even_squares)

alt = list(map(lambda x: x**2, filter(lambda x: x%2 == 0, a)))
print(alt)
assert even_squares == alt#assert 陳述在程式中安插除錯用的斷言（Assertion）檢查時很方便的一個方式。
print(even_squares)


chile_ranks = {'ghost':1, 'habanero':2, 'cayenne':3}
rank_dict   = {rank: name for name, rank in chile_ranks.items()}
chile_len_set = {len(name) for name in rank_dict.values()}
print(rank_dict)
print(chile_len_set)