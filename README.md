# Python Learning Manager

这个库用于管理 Python 学习代码，例如按章节整理练习、快速列出章节目录、查找示例文件。

## 安装

在当前目录运行：

```powershell
python -m pip install -e .
```

## 使用

```python
from python_learning_manager import LearningLibrary

library = LearningLibrary(".")
print(library.list_chapters())
print(library.list_python_files())
```

现有的 `Chapter1`、`Chapter2`、`Chapter3`、`Chapter4` 目录会保持原样，可以继续往里面放学习代码。

