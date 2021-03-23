"""
This is even more bugged than Cyberpunk 2077 was at release
"""
import argparse
import pathlib
import typing as tp

Node = tp.Tuple[str, str]  # links

"""
Counting entrances quantity
"""
def traverse(graph: tp.List[Node]):
    i = -1
    self_ref: tp.List[tp.Tuple[Node, int]] = []
    for link in graph:
        i += 1
        if link[0] == link[1]:
            self_ref.append((link, i))

    if len(self_ref) != 0:
        return (self_ref[0][0][0], graph[self_ref[0][1] + 1][0])

    if graph[i][1] != graph[0][0]:
        graph[i] = (graph[i][0], graph[0][0])

    return graph[i]


def load_tasks(taskfile: str = "tasks.txt") -> tp.List[tp.List[Node]]:
    res: tp.List[tp.List[Node]] = []
    exclude: tp.List[int] = []
    path = pathlib.Path(taskfile)
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f.readlines()):
            if line[:4] == "task":
                pos = line[4]
                res.insert(int(pos), [])
                exclude.append(i)
        f.seek(0)  # revert to file start
        skip_pos = -1
        for i, line in enumerate(f.readlines()):
            if i in exclude:
                skip_pos += 1  # offset
                continue
            if "->" in line:  # link
                res[skip_pos].append((line[0], line[5]))

    return res


def flat_letters(graph: tp.List[Node]) -> tp.List[str]:
    letters = [[letter for letter in line] for line in graph]
    flat_letters = [j for i in letters for j in i]
    return flat_letters


def check_broken_links(graph: tp.List[Node]) -> int:
    """
    Returns count of broken links
    """
    # 2 of each letter in graph
    # each link is unique
    letters: tp.Dict[str, int] = {}  # count of letter
    letters_count = len(set(flat_letters(graph)))
    broken_links: tp.List[Node] = []
    if not letters_count == len(graph):
        raise ValueError("Well, samurai...")
    broken = 0
    for link in graph:
        if link[0] == link[1]:
            broken_links.append(link)
            broken += 1
        for letter in link:
            if not letter in letters.keys():
                letters[letter] = 0
            letters[letter] += 1

    for i, count in enumerate(letters.values()):
        if i == 0:  # skip loop to a
            continue
        if count > 2:
            broken += 1

    return broken


def main():
    parser = argparse.ArgumentParser(description="Bugged quests")
    parser.add_argument(
        "quest_log", help="Path to questlog", default="tasks.txt", nargs="?", type=str
    )
    args = parser.parse_args()
    tasks = load_tasks(args.quest_log)
    for graph in tasks:
        broken = check_broken_links(graph)
        if broken != 1:
            print("V, V, V...")
        else:
            fix = traverse(graph)
            print(f"{fix[0]} -> {fix[1]}")

main()
