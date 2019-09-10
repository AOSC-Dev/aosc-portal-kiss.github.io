import redis
import sys
import json
import datetime
import slug


def list_all_news(server):
    return server.keys('news:item:*')


def get_filename(key, value):
    try:
        timestamp = int(key[10:]) // 1000
        timestamp = datetime.datetime.utcfromtimestamp(timestamp)
        titile_slug = slug.slug(value.get('title'))
        return '%s-%s.md' % (timestamp.strftime('%Y-%m-%d'), titile_slug)
    except Exception:
        return None


def escape_title(title):
    if title.find("'") >= 0:
        return '"%s"' % title.replace('"', '\\"')
    return "'%s'" % title


def write_file(filename, value):
    news_type = value.get('type')
    important = 'false'
    if news_type == 'bug':
        important = 'true'
        news_type = 'news'
    if news_type not in ['news', 'community']:
        print('Unknown news type: %s' % news_type)
    with open(filename, 'wt') as f:
        f.write('---\nlayout: post\ntitle: %s\ntype: %s\nimportant: %s\n---\n\n' %
                (escape_title(value.get('title')), news_type, important))
        f.write(value.get('content'))


def main():
    if len(sys.argv) < 2:
        print('Usage: %s <output directory>' % sys.argv[0])
        return
    path = sys.argv[1]
    server = redis.Redis(host='localhost')
    keys = list_all_news(server)
    done = 0
    print('Found %s entries' % len(keys))
    print('Exporting to %s...' % path)
    for k in keys:
        value = server.get(k)
        value = json.loads(value)
        filename = get_filename(k, value)
        if filename is None:
            continue
        done += 1
        write_file('%s/%s' % (path, filename), value)
    print('... %s converted' % done)



if __name__ == "__main__":
    main()
