#!/usr/bin/env python

import sys
import json


def main():
    artists = json.load(open(sys.argv[1]))['artists']
    res = []

    for artist in artists:
        d = {'model': 'art.artist', 'fields': artist}
        res.append(d)

    print(json.dumps(res))

if __name__ == '__main__':
    main()
