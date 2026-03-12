# CubeHello 项目说明

## 项目概述
这是一个简单的 Python 演示项目，用于学习 Claude Code + GitHub 协作流程。

## 技术栈
- Python 3.10+
- 无外部依赖

## 代码规范
- 函数必须有 type hints 和 docstring
- commit message 使用中文，格式为：`<类型>: <描述>`
  - 类型包括：feat(新功能), fix(修复), docs(文档), refactor(重构), test(测试)
- 每次提交前确保代码能正常运行

## 项目结构
- main.py: 主程序入口
- README.md: 项目说明

## Git 工作流
- 主分支为 main
- 新功能在 feature/ 分支上开发
- 通过 Pull Request 合并到 main