from collections.abc import Iterator
from dataclasses import dataclass, field
import itertools
from typing import Optional


@dataclass
class File:
    name: str
    parent: Optional['Directory']
    
    def __repr__(self) -> str:
        # Use format from the exercise description
        return self.__str__()


@dataclass
class Directory(File):
    children: dict[str, File] = field(default_factory=dict)
    
    def __str__(self) -> str:
        return f"{self.name} (dir)"

    @property
    def size(self):
        return sum(child.size for child in self.children.values())
    
    def walk(self) -> Iterator[File]:
        it = iter((self,))
        for child in self.children.values():
            if isinstance(child, Directory):
                it = itertools.chain(it, child.walk())
            else:
                it = itertools.chain(it, (child,))
        return it


@dataclass
class PlainFile(File):
    size: int
    
    def __str__(self) -> str:
        return f"{self.name}, (file, size={self.size})"


root = Directory('', None)
with open('input', 'r') as f:
    for line in f:
        match line.split():
            case ['$', command, *args]:
                current_command = [command, *args]
                match current_command:
                    case ['cd', '..']:
                        current_directory = current_directory.parent
                    case ['cd', '/']:
                        current_directory = root
                    case ['cd', x]:
                        current_directory = current_directory.children[x]
            case output:
                match current_command:
                    case ['ls']:
                        match output:
                            case ['dir', xyz]:
                                if xyz not in current_directory.children:
                                    current_directory.children[xyz] = Directory(xyz, current_directory)
                            case [size, abc]:
                                if abc not in current_directory.children:
                                    current_directory.children[abc] = PlainFile(abc, current_directory, int(size))

print(sum(map(lambda f: f.size, filter(lambda f: isinstance(f, Directory) and f.size <= 100000, root.walk()))))

total = 70000000
required = 30000000
unused = total - root.size
to_delete = required - unused
candidates = filter(lambda f: isinstance(f, Directory) and f.size >= to_delete, root.walk())
print(sorted(candidates, key=lambda f: f.size)[0].size)
