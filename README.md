# Shout_Scrap
Ast4u.me Shoutbox Scrapper

This is a program to scrap (ie. read stuff that were originally intended to be used between web-server and web-browser) a shoutbox style web-chat build for the website: https://ast4u.me

This is an invite-only website, but the code might still serve as an example how to scrap ajax transported json data.

Usage example:

```
$ ./read_shout.py --help
Usage: read_shout.py [-t timestamp]

Ast4u.me Shoutbox Scrapper.

Options:
  -h, --help            show this help message and exit
  -t TIMESTAMP, --timestamp=TIMESTAMP
                        set specific unix timestamp since when messages should
                        be returned. Defaults to current time.
  -d DEBUG, --debug=DEBUG

$ ./read_shout.py -t 1480001354
1480088475
Cool!  Es wurde ein Torrent hochgeladen: L....MP3.DL.BluRay.xvid-AST4u
Cool!  Es wurde ein Torrent hochgeladen: L....AC3.DL.720p.BluRay.x264-AST4u
Cool!  Es wurde ein Torrent hochgeladen: L....AC3.DL.1080p.BluRay.x264-AST4u
Cool!  Es wurde ein Torrent hochgeladen: L....DTS.DL.1080p.BluRay.x264-AST4u
```
