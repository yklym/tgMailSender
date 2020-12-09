def text_to_snake(text):
    return text.split(' ').join('_')


def text_from_snake(text):
    return text.split('_').join(' ')
