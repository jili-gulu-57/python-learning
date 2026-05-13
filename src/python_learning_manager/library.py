"""Small utilities for organizing Python learning folders."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class PythonFile:
    """A Python source file discovered in the learning library."""

    path: Path
    chapter: str | None


class LearningLibrary:
    """Browse a directory that stores Python learning code by chapter."""

    def __init__(self, root: str | Path) -> None:
        self.root = Path(root).expanduser().resolve()

    def list_chapters(self) -> list[str]:
        """Return chapter-like directories sorted by name."""
        if not self.root.exists():
            return []

        return sorted(
            path.name
            for path in self.root.iterdir()
            if path.is_dir() and path.name.lower().startswith("chapter")
        )

    def list_python_files(self, chapter: str | None = None) -> list[PythonFile]:
        """Return Python files from the whole library or one chapter."""
        search_root = self.root / chapter if chapter else self.root
        if not search_root.exists():
            return []

        files: list[PythonFile] = []
        for path in sorted(search_root.rglob("*.py")):
            relative = path.relative_to(self.root)
            chapter_name = relative.parts[0] if relative.parts else None
            files.append(PythonFile(path=path, chapter=chapter_name))
        return files

