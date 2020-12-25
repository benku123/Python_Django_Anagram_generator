from django.shortcuts import render

from itertools import permutations


# Create your views here.
def anagram_form(request):
    search_query = request.GET.get('search')
    anagram_text = ['Here you will see your anagram']
    if search_query:
        anagram_text = sorted(set(''.join(i) for i in permutations(list(search_query))))
    return render(request, 'word_solver/anagram.html', context={'anagram_text': anagram_text, 'title': 'Anagram'})


def palindrome(request):

    palindrome_text = request.GET.get('palindrome')
    if palindrome_text:
        palindrome_converted = ' '.join(i[::-1] for i in palindrome_text.split())
    context = {
        'title': 'Palindrome',
        'palindrome_text': palindrome_text,
        'palindrome_converted': palindrome_converted,
    }
    return render(request, 'word_solver/palindrome.html', context)
