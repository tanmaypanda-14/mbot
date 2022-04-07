# Music recommender chatbot

### installation
make a authorisation.py file in ./utils and add the following code
```
import tekore as tk


def authorize():
    client_id = ''
    client_secret = ''
    app_token = tk.request_client_token(client_id, client_secret)
    return tk.Spotify(app_token)
```
- client_id and client_secret fields are to be filled with theie respective values from the spotify app developer portal

Also the following packages are to be installed as dependencies

```
pip install tekore discord.py pandas numpy scikit-learn billboard.py
```

### Working

When provided with a song name the model scrapes energy and valence data from spotify via the api and makes a vector. This vector can be visualized like a graph
where energy and valence are respective axes and using the scraped data the model plots all the values on this graph. Then using scaling the values are scaled to 100x and
distances between every point is found and the 5 closest distance from our input song is returned.

### Usage 

- $recommend <song name>       // returns 5 songs similar to the input song
- $top5          // returns top 5 trending songs on billboard
  
