from django.shortcuts import render

from itertools import permutations


def generator_anagram(word):
    """stands for yielding 1 words at a time"""
    for i in permutations(word, len(word)):
        yield ''.join(i)


def anagram_form(request):
    search_query = request.GET.get('search')
    number_of_outputs = request.GET.get("limitation")
    anagram_text = 'Here you will see your anagram'
    list_of_words = []

    if number_of_outputs:
        number_of_outputs = int(number_of_outputs)
    else:
        number_of_outputs = 10

    if search_query:
        words = generator_anagram(search_query)
        for i in range(number_of_outputs):
            try:
                list_of_words.append(''.join(next(words)))
            except StopIteration:
                break

    return render(request, 'word_solver/anagram.html', context={'list_of_words': list_of_words,
                                                                'anagram_text': anagram_text,
                                                                'title': 'Anagram'})
