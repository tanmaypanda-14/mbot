from recommendationmodel import *
import utils.authorization as auth

sp=auth.authorize()

def suggestion_system_func(song) :
    results = sp.search(song, types=('track',), limit=5)
    Song_info = results[0].asbuiltin()

    Search_result = []
    for i in range(0, 5):
        Search_result.append((Song_info['items'][i]['name'] + " by " + Song_info['items'][i]['artists'][0]['name']))

    for i in range(0, 5):
        print(str(i + 1) + "." + Song_info['items'][i]['name'] + " by " + Song_info['items'][i]['artists'][0]['name'])

    choice = int(input("Enter Song No."))

    ch_id = Song_info['items'][choice - 1]['id']

    return recommend(track_id=ch_id, ref_df=df, sp=sp, n_recs=5)

