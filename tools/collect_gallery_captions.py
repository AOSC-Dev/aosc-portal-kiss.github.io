import yaml
import toml


def main():
    gallery = yaml.safe_load(open('./data/gallery.yml'))['gallery']
    trans = toml.load(open('./i18n/en.toml'))
    for i in gallery:
        for j in i['album']:
            msg_id = j['file'].split('.')[0]
            if not trans.get(msg_id):
                print("[{}]\nother = \"{}\"".format(msg_id, j['desc']))


if __name__ == "__main__":
    main()
