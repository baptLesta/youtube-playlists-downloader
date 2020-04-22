#!/usr/bin/env python2

import os
from dotenv import load_dotenv

load_dotenv()

FOLDER_PATH = os.getenv("FOLDER_PATH")

playlists = [
    "https://music.youtube.com/playlist?list=PLXWtlchonpjzgnUf4nvxl_5u5tE9nYleE", # Repetiv dancing house
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
    "https://music.youtube.com/playlist?list=PLXWtlchonpjwIqhhHgsKUO79E477v8hr-", # Hummer
    "https://music.youtube.com/playlist?list=PLXWtlchonpjwd8J_wsfu9s1GAuZyEgfK-", # Step By aside
    "https://music.youtube.com/playlist?list=PLXWtlchonpjwv9GBF4QTWqoKMwiULceXx", # Diforme
    "https://music.youtube.com/playlist?list=PLXWtlchonpjxgHKiCgYOv6iyrgGiAq1gX", # Italo, retro
    "https://music.youtube.com/playlist?list=PLXWtlchonpjwfK_luAnJf_if7lHVN02d9", # Piano
    "https://music.youtube.com/playlist?list=PLXWtlchonpjxIevzOG3hMgT2ecATmMI58", # Shampoing
    "https://music.youtube.com/playlist?list=PLXWtlchonpjwl3I1nX58JuAcWN2PEF2AE", # Indie
    "https://music.youtube.com/playlist?list=PLXWtlchonpjzBUyN0BvDd_w36zKVkZ_wD", # Sunny vibe
    "https://music.youtube.com/playlist?list=PLXWtlchonpjx4PJd_8s8PK_BtpPV5yY1F", # New Wave Vocal
    "https://music.youtube.com/playlist?list=PLXWtlchonpjwg6hv54O0pkSKOneOscpRV", # Melodic Vocal
    "https://music.youtube.com/playlist?list=PLXWtlchonpjwyVIZbYUp1r9yT3xaFmZ_A", # Transition Bass Dark
    "https://music.youtube.com/playlist?list=PLXWtlchonpjzvI56sNyq6CMUy7FQXVJTe", # In da Bowling
    "https://music.youtube.com/playlist?list=PLXWtlchonpjyj9-8ftB-5fVXC_8r6V_Pf", # Kraby Dark
    "https://music.youtube.com/playlist?list=PLXWtlchonpjyTFFv04iab_BgBF_Wiq7gL", # Eden Hasard
    "https://music.youtube.com/playlist?list=PLXWtlchonpjznOQ7SMugdNENUZjsvfA34", # Envole Lyrique
    "https://music.youtube.com/playlist?list=PLXWtlchonpjw3cIqf5fO7gONlFyjcjamb", # Down Temp Electronica
    "https://music.youtube.com/playlist?list=PLXWtlchonpjxPyCyKunwPOwELb4BAXQ5_", # Repetiv House
    "https://music.youtube.com/playlist?list=PLXWtlchonpjyqi8V1cmIVjwv4azXMy6CG", # Patinette
    "https://music.youtube.com/playlist?list=PLXWtlchonpjwfK_luAnJf_if7lHVN02d9", # Piano
    "https://music.youtube.com/playlist?list=PLXWtlchonpjyuHnGPo5yrmH-lG7JxyIFG", # Hop House
    "https://music.youtube.com/playlist?list=PLXWtlchonpjzuYMcea22Uff_lT_Xh0C0x", # Loklass
]

for playlistLink in playlists:
     os.system("youtube-dl --download-archive archive.txt --embed-thumbnail --extract-audio --audio-format mp3 --add-metadata  -o \"{}/%(playlist)s/%(title)s.%(ext)s\" -i {}".format(FOLDER_PATH, playlistLink))



