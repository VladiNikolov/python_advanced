def add_songs(*tuples):
    songs_dict = {}

    for element in tuples:
        song, lyrics = element

        if song not in songs_dict:
            songs_dict[song] = []

        songs_dict[song].extend(lyrics)

    output = []

    for s_title, s_lyrics in songs_dict.items():
        output.append("- " + s_title)
        output.extend(s_lyrics)

    return "\n".join(output)
