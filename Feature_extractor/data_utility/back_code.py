"""
The below code is for tmdb connection
"""



### Example: taking 'the matrix' film as an example'

mov = tmdb.Movies(603)

mov_info = mov.info()


mov_info['title']

mov_info["poster_path"]

pre_fix = 'http://image.tmdb.org/t/p/w185//'
download_path = "/Users/zishuoli/Doc/project/Feature_extractor/Image/"
path1 = 'lh4aGpd3U9rm9B8Oqr6CUgQLtZL.jpg'
path2 = 'hEpWvX6Bp79eLxY1kX5ZZJcme5U.jpg'
print(pre_fix+path1)
print(pre_fix+path2)
