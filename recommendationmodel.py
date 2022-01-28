import pandas as pd
import utils.authorization as auth
import numpy as np
from numpy.linalg import norm

df = pd.read_csv("/mnt/d/repos/whoebot/datasets/SpotifyFeatures.csv")

df["mood_vec"] = df[["valence", "energy"]].values.tolist()
df["mood_vec"].head()

sp = auth.authorize()


def recommend(track_id, ref_df, sp, n_recs=5):
    track_features = sp.track_audio_features(track_id)
    track_moodvec = np.array([track_features.valence, track_features.energy])

    ref_df["distances"] = ref_df["mood_vec"].apply(lambda x: norm(track_moodvec - np.array(x)))
    ref_df_sorted = ref_df.sort_values(by="distances", ascending=True)
    ref_df_sorted = ref_df_sorted[ref_df_sorted["id"] != track_id]

    ans=ref_df_sorted.iloc[:n_recs]
    
    return ans 
    
