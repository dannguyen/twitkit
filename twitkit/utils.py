from rich.console import Console
# from rich.syntax import Syntax
import json
import sys
from sys import stderr


def myprint(*args, **kwargs):
    if len(args) == 1 and type(args[0]) in (dict, list):
        # special case where there's only one printed argument, and the argument may be
        #  something like a dict or a list that we want pretty indented
        # stderr.write("1 dict/list argument\n")

        txt = json.dumps(args[0], indent=2)
        if not sys.stdout.isatty():
            # We're piping to file, so just use standard print
            # stderr.write("standard print\n")
            print(txt)
        else:
            # stderr.write("rich print\n")
            # sx = Syntax(txt, lexer_name='json', code_width=999)
            console = Console()
            console.print(txt, **kwargs)
    else:
        # stderr.write("several args\n")
        # stderr.write("rich print\n")
        # many arguments, not necessarily syntax specific
        console = Console()
        console.print(*args, **kwargs)


    # TK: probably a more efficient way to customize this, built within the Rich.console library


# https://stackoverflow.com/questions/5067604/determine-function-name-from-within-that-function-without-using-traceback

# import inspect
# def footest(*args, **kwargs):
#     fooname = inspect.stack()[0][3]
#     xargs = args
#     if len(xargs) > 0:
#         print(f"{fooname} has {len(args)} arguments:")
#         for val in xargs:
#             print(f"\t{str(val)}")
#     yargs = kwargs.items()
#     if len(yargs) > 0:
#         print(f"{fooname} has {len(yargs)} keyword arguments:")
#         for k, v in yargs:
#             print(f"\t{str(k)}", ":", v)

# footest(1,2,3,4, hey='daddy', bye='world')
# data = {'created_at': 'Tue Mar 21 20:50:14 +0000 2006', 'id': 20, 'id_str': '20', 'text': 'just setting up my twttr', 'truncated': False, 'entities': {'hashtags': [], 'symbols': [], 'user_mentions': [], 'urls': []}, 'source': '<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'user': {'id': 12, 'id_str': '12', 'name': 'jack', 'screen_name': 'jack', 'location': '', 'description': '#bitcoin', 'url': None, 'entities': {'description': {'urls': []}}, 'protected': False, 'followers_count': 4723057, 'friends_count': 4448, 'listed_count': 27536, 'created_at': 'Tue Mar 21 20:50:14 +0000 2006', 'favourites_count': 28597, 'utc_offset': None, 'time_zone': None, 'geo_enabled': True, 'verified': True, 'statuses_count': 26957, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'EBEBEB', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme7/bg.gif', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme7/bg.gif', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1115644092329758721/AFjOr-K8_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1115644092329758721/AFjOr-K8_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/12/1584998840', 'profile_link_color': '990000', 'profile_sidebar_border_color': 'DFDFDF', 'profile_sidebar_fill_color': 'F3F3F3', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': True, 'default_profile': False, 'default_profile_image': False, 'following': True, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'regular'}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 115840, 'favorite_count': 131489, 'favorited': False, 'retweeted': False, 'lang': 'en'}
