from django import template

register = template.Library()

bad_words = ['редиска', 'breaking', 'clever']

@register.filter()
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
