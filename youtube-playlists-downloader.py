import os

playlists = [
    "https://music.youtube.com/playlist?list=PLXWtlchonpjxPF4_YrGoQDMXQeP39ufKc", # Repetiv dancing house
    "https://music.youtube.com/playlist?list=PLXWtlchonpjwtAu00PDSNAwZGFKkpkN4L", # Oscilloscope
    "https://music.youtube.com/playlist?list=PLXWtlchonpjxPF4_YrGoQDMXQeP39ufKc", # Transition Light
    "https://music.youtube.com/playlist?list=PLXWtlchonpjwLzSqgdmUSha6_ZNZeB8ND", # Disco soul and beats
    "https://music.youtube.com/playlist?list=PLXWtlchonpjzqzXIKuxZXoL2FQoZJ08LZ", # Elektek
    "https://music.youtube.com/playlist?list=PLXWtlchonpjwAMqPtfQbx9k-4HoXBYl8J", # Arpegiator
    "https://music.youtube.com/playlist?list=PLXWtlchonpjx3_Rsk6mGtJnlmKz34Fpvn", # Kraby is Dancing
    "https://music.youtube.com/playlist?list=PLXWtlchonpjz2ouY6ZF_djt7qZGrccZjA", # Vaisselle motivation
    "https://music.youtube.com/playlist?list=PLXWtlchonpjz5lyeLl6blHNchudcCltRb", # Sleepy
    "https://music.youtube.com/playlist?list=PLXWtlchonpjxJ01JKdeejjNPxtSxJOiFB", # NightWalk
    "https://music.youtube.com/playlist?list=PLXWtlchonpjwkiOe5Qv3l6Kp1Pn3Ssaan", # Transition Dark
    "https://music.youtube.com/playlist?list=PLXWtlchonpjygzE-_SJLYisk7UGpbK9ut", # Exception Remix
    "https://music.youtube.com/playlist?list=PLXWtlchonpjzvwb0mhk-_G_qP4cLiiq3K", # Exception 
    "https://music.youtube.com/playlist?list=PLXWtlchonpjxtFTvHyNMYa1RYz9OZHnWr", # Border
    "https://music.youtube.com/playlist?list=PLXWtlchonpjxx3e-kWx3jTaPjMDwh0PrD", # Ambiance
    "https://music.youtube.com/playlist?list=PLXWtlchonpjx5hZpacp6YMBBI4TWypyAW", # Kraby
    "https://music.youtube.com/playlist?list=PLXWtlchonpjwwaGgZOoa2IPoz1Qdbq6-F", # Pride
    "https://music.youtube.com/playlist?list=PLXWtlchonpjwIqhhHgsKUO79E477v8hr-", # Step By aside
]

for playlistLink in playlists:
     os.system("youtube-dl -o \"~/Documents/Musique/Youtube Lib/%(playlist)s/%(title)s.%(ext)s\" -i {}".format(playlistLink))



