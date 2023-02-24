# to download the required libraries use this command pip install -r  requirements.txt
from googleapiclient.discovery import build
import config

"""this function take API_KEY & KEYWORD and return a list of dic (result)"""


def Search(key, keyWords, n, ord, typ):
    suffix = id = ''
    if typ == 'video':
        suffix = 'watch?v='
        id = 'videoId'
    elif typ == 'channel':
        suffix = 'channel/'
        id = 'channelId'
    elif typ == 'playlist':
        suffix = 'playlist?list='
        id = 'playlistId'
    youtube = build('youtube', 'v3', developerKey=key)
    requist = youtube.search().list(order=ord,
                                    q=keyWords, part='snippet', type=typ, maxResults=n)

    response = requist.execute()

    response_list = []  # create list to store result
    urlf = "https://www.youtube.com/{}{}"  # string variable to generate the url
    for item in response['items']:  # append the result to the list in dictionary format
        response_list.append(
            {'name': item['snippet']['title'],
             'url': urlf.format(suffix, item['id'][id])})
    return response_list  # the result


if __name__ == "__main__":
    my_key = config.key
    keyword = 'api'  # write what you are looking for in this variable
    num = 3  # max number of result
    type = 'video'  # choose one element from the following list to filter the search
    # ['video', 'channel', 'playlist']
    order = 'date'  # choose one element from the following list to filter the search
    # ['date', 'rating', 'relevance', 'title', 'videoCount']
    result_list = Search(my_key, keyword, num, order,type)  # call the function
    print(f'the result about: "{keyword}"')
    for result in result_list:
        print(f"video name:{result['name']}")
        print(f"URL={result['url']}\n")
