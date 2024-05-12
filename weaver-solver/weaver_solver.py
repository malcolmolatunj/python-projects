import argparse

import networkx as nx
from networkx.exception import NodeNotFound, NetworkXNoPath


def differs_by_one_letter(word1: str, word2: str) -> bool:
    num_differing_lettters = sum(l1 != l2 for l1, l2 in zip(word1, word2))
    return num_differing_lettters == 1


def get_word_graph(filename: str) -> nx.Graph:
    with open(filename) as f:
        words = [word.rstrip() for word in f.readlines()]

    graph = nx.Graph()
    for i, word in enumerate(words, start=1):
        for other_word in words[i:]:
            if differs_by_one_letter(word, other_word):
                graph.add_edge(word.upper(), other_word.upper())
    return graph


def main() -> None:
    parser = argparse.ArgumentParser(description="Solves Weaver puzzles")
    parser.add_argument("source", type=str, help="the first word given in the puzzle")
    parser.add_argument("target", type=str, help="the target word shown in the puzzle")
    args = parser.parse_args()

    if len(args.source) != len(args.target):
        raise ValueError("Source and target must be of same length")

    if len(args.source) == 4:
        filename = "4-letter-words.txt"
    elif len(args.source) == 5:
        filename = "5-letter-words.txt"
    else:
        raise ValueError("No dictionary available for words of this length!")

    graph = get_word_graph(filename)
    try:
        path = nx.shortest_path(graph, args.source.upper(), args.target.upper())
    except NodeNotFound:
        print(f"Either {args.source} or {args.target} was not found in the dictionary.")
        print(
            "If they are in the dictionary, then they are not one letter away from other words."
        )
    except NetworkXNoPath:
        print(f"No path found between {args.source} and {args.target}")
    else:
        print(path)


if __name__ == "__main__":
    main()
