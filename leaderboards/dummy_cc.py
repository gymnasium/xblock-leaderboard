"""
Dummy comment client module, used for testing.
"""


def make_thread_dict(number, points):
    return {
        'title': 'Thread {}'.format(number),
        'votes': {'point': points},
        'id': number,
        'username': 'user{}'.format(number)
    }

varied_votes = (0, 4, 8, 6, 3, 5, 4, 6, 4, 2, 0, 1)
# Dictionary of dummy threads to return when using thread.search.
test_ids = {
    'many_threads': [make_thread_dict(i, i) for i in xrange(1, 30)],
    'unvoted_threads': [make_thread_dict(i, 0) for i in xrange(1, 5)],
    'varied_voting': [make_thread_dict(i, varied_votes[i]) for i in xrange(0, 10)]
}

for value in test_ids.values():
    value.sort(key=lambda x: x['votes']['point'], reverse=True)


class Thread(object):
    """
    Dummy version of commment client thread that returns test thread dicts.
    """
    @staticmethod
    def search(search_dict):
        end = search_dict['per_page']
        # Could be 0.
        end = end and end + 1
        commentable_id = search_dict['commentable_id']
        if commentable_id not in test_ids:
            return [[]]
        return [test_ids[commentable_id][0:end]]
