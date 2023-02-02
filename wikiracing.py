import wikipediaapi
from typing import List


class WikiRacer:

    def __init__(self) -> None:
        pass
    def find_path(self, start: str, finish: str) -> List[str]:
        wiki = wikipediaapi.Wikipedia(language='uk', extract_format=wikipediaapi.ExtractFormat.WIKI)

        start = wiki.page(start)
        end = wiki.page(finish)

        if not start.exists() or not end.exists():
            return None

        visited = set()
        queue = [(start, [start.title])]
        while queue:
            (curr, path) = queue.pop(0)
            if curr.title in visited:
                continue
            visited.add(curr.title)
            for link in curr.links:
                if link in visited:
                    continue
                if link == end.title:
                    return path + [end.title]
                queue.append((wiki.page(link), path + [link]))

