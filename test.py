from youtube_search import YoutubeSearch
#from main import searcher

def searcher(text):
    res = YoutubeSearch(text, max_results=1).to_dict()
    print(res)
    return res


def test_Searcher():
    search_list = ["pepe the frog - music clip", "Валерий Меладзе - Салют, Вера"]
    answer = [{'id': 'vJMP7RBsoms', 'thumbnails': ['https://i.ytimg.com/vi/vJMP7RBsoms/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLAdscd5RtMB7g8mF3yRyq6W4rXZow', 'https://i.ytimg.com/vi/vJMP7RBsoms/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLD4XGjj19jucNVNC00Wlc7wGDdIMA'], 'title': "Pepe the frog - music clip (Marvel83' - Golden Dawn)", 'long_desc': None, 'channel': 'sad pepe frog', 'duration': '5:02', 'views': '2\xa0098\xa0486 просмотров', 'publish_time': '11 месяцев назад', 'url_suffix': '/watch?v=vJMP7RBsoms'}, {'id': '8x1U_WU8bV0', 'thumbnails': ['https://i.ytimg.com/vi/8x1U_WU8bV0/hqdefault.jpg?sqp=-oaymwEjCOADEI4CSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLDNDqNc_3ho3xMB569sxJ-SxAsHEw'], 'title': 'Валерий Меладзе - Салют, Вера', 'long_desc': None, 'channel': 'meladzeofficial', 'duration': '3:49', 'views': '313\xa0887 просмотров', 'publish_time': '12 лет назад', 'url_suffix': '/watch?v=8x1U_WU8bV0'}]
    for ind, search in enumerate(search_list):
        res = searcher(search)[0]
        for key in res.keys():
            if key != 'views':
               assert res[key] == answer[ind][key]
