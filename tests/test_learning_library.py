from python_learning_manager import LearningLibrary


def test_list_chapters(tmp_path):
    (tmp_path / "Chapter1").mkdir()
    (tmp_path / "notes").mkdir()

    library = LearningLibrary(tmp_path)

    assert library.list_chapters() == ["Chapter1"]


def test_list_python_files(tmp_path):
    chapter = tmp_path / "Chapter1"
    chapter.mkdir()
    source = chapter / "hello.py"
    source.write_text("print('hello')\n", encoding="utf-8")

    files = LearningLibrary(tmp_path).list_python_files()

    assert len(files) == 1
    assert files[0].path == source
    assert files[0].chapter == "Chapter1"

