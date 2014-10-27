#!/usr/bin/env python
#coding:utf8


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "d1.settings")

from vine_comment.models import Url, Tag
import argparse


parser = argparse.ArgumentParser(description='Url Tag Combination Client.')
parser.add_argument('-a', '--add', help='add url tag combination', nargs=2, metavar=('url', 'tag'))
parser.add_argument('-r', '--rem', help='rem url tag combination', nargs=2, metavar=('url', 'tag'))
parser.add_argument('-g', '--get', help='get url tag combination', nargs=2, metavar=('url', 'tag'))
parser.add_argument('-gu', '--getu', help='get url tag combination', nargs=1, metavar=('url'))
parser.add_argument('-gt', '--gett', help='get url tag combination', nargs=1, metavar=('tag'))
parser.add_argument('-m', '--mod', help='mod url tag combination', nargs=2, metavar=('url', 'tag'))

cmds = ['add', 'rem', 'get', 'mod', 'gett']
short_cmds = ['a', 'r', 'g', 'm', 'gt']

class TagManager(object):
    @staticmethod
    def add(url, tag):
        url, u_created = Url.objects.get_or_create(url=url, content=url)
        url_tag, ut_created = Tag.objects.get_or_create(name=tag)
        url_tag.urls.append(url.id)
        url_tag.save()

    @staticmethod
    def rem(url, tag):
        url_tags = Tag.objects.filter(name=tag)
        for url_tag in url_tags:
            url_tag.delete()

    @staticmethod
    def get(url, tag):
        url_tags = Tag.objects.filter(name=tag)
        import pdb; pdb.set_trace()
        for url_tag in url_tags:
            print(url_tag.name, url_tag.urls)
            for url in url_tag.urls:
                url_object = Url.objects.filter(id=url)
                print(url_object)

    @staticmethod
    def gett(tag):
        url_tags = Tag.objects.filter(name=tag)
        for url_tag in url_tags:
            print(url_tag.name, url_tag.urls)
            for url in url_tag.urls:
                url_object = Url.objects.filter(id=url)
                print(url_object)

    @staticmethod
    def getu(url):
        all_url_tag = Tag.objects.all()
        for url_tag in all_url_tag:
            for saved_url in url_tag.urls:
                if url == saved_url:
                    print(url_tag)

    @staticmethod
    def mod(*args, **kwargs):
        pass

def main():
    args = vars(parser.parse_args())
    print("args: " + str(args))

    for key in args:
        if args[key] is None:
            continue
        print(key+' '+str(args[key]))
        func = getattr(TagManager, key)
        if len(args[key]) == 1:
            result = func(args[key][0])
        elif len(args[key]) == 2:
            result = func(args[key][0], args[key][1])

if __name__ == '__main__':
    main()

