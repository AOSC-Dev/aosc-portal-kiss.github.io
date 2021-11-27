import yaml
import os
import sys


def generate_stubs(name: str, type='404', link=None):
    if link is None:
        link = 'https://github.com/{}/'.format(name)
    template = """---\nlayout: people_{type}\nlink: {link}\nurl: /people/~{name}/\n---\n<!-- Automatically generated -->\n"""
    return template.format(name=name, type=type, link=link)


def what_to_generate(yml, listing):
    needed = set([(i["username"], i["rurl"]) for i in yml])
    difference = set()
    existing = set()
    for item in listing:
        existing.add(item.replace('.html', '').replace('.md', ''))
    for need in needed:
        if need[0] not in existing:
            difference.add(need)
    return difference


def parse_yml(filename: str):
    with open(filename, 'r') as f:
        results = yaml.safe_load(f)
    return results


def main():
    if len(sys.argv) < 3:
        print("Usage: python {} [path/to/people.yml] [path/to/people/]".format(sys.argv[0]))
        return
    missing_people = what_to_generate(parse_yml(sys.argv[1]), os.listdir(sys.argv[2]))
    if len(missing_people) == 0:
        print("Nothing to do.")
        return
    print("Need to generate templates for {} people".format(len(missing_people)))
    for person in missing_people:
        name, url = person
        print('Generating template for {}... '.format(name), end="")
        content = generate_stubs(name, '302' if url else '404', url)
        with open(os.path.join(sys.argv[2], '%s.html' % name), 'wt') as f:
            f.write(content)
        print('Done!')


if __name__ == "__main__":
    main()
