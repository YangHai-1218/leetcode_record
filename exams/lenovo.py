# paper_num = int(input())
# author_scores = dict()
# for i in range(paper_num):
#     input_ = input().split(' ')
#     author_num = int(input_[0])
#     for j in range(author_num):
#         author = input_[j+1]
#         if author not in author_scores:
#             author_scores[author] = 3 - j
#         else:
#             author_scores[author] += 3 - j
# authors = sorted(author_scores.keys())
# for author in authors:
#     print(f"{author} {author_scores[author]}")
n, k = map(lambda x:int(x), list(input().split(' ')))
number = input()
number_list  = [int(d) for d in str(number)]
if k == 0:
    number_list.append(0)
else:
    for j in range(len(number_list)):
        if number_list[j] < k:
            number_list.insert(j, k)
            break
    if len(number_list) == n:
        number_list.append(k)
print(int("".join([str(d) for d in number_list])))
