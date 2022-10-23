bad_words = ['писики', 'breaking']
def madness(value):
    text_split = value.split()
    iter = -1
    for x in text_split:
        iter += 1
        if x in bad_words:
            for_len_x = (len(x) - 1) * '*'
            x = x.replace(x[1:], for_len_x)
            text_split[iter] = x
    return f'{" ".join(text_split)}'

print(madness('редиска сиски писики'))

# value = 'редиска сиски писики'
# text_split = value.split()
# iter = -1
# for x in text_split:
#     iter += 1
#     if x in bad_words:
#         for_len_x = (len(x) - 1) * '*'
#         x = x.replace(x[1:], for_len_x)
#         text_split[iter] = x
# print(*text_split)


