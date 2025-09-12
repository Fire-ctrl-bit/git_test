# Git 学习测试仓库 (Git Learning Test Repository)

这是一个用于学习和练习 Git 操作的测试仓库。

## 基础 Git 命令 (Basic Git Commands)

### 1. 仓库初始化 (Repository Initialization)
```bash
git init                    # 初始化新仓库
git clone <url>            # 克隆远程仓库
```

### 2. 文件操作 (File Operations)
```bash
git add <file>             # 添加文件到暂存区
git add .                  # 添加所有更改
git commit -m "message"    # 提交更改
git status                 # 查看仓库状态
git diff                   # 查看更改差异
```

### 3. 分支操作 (Branch Operations)
```bash
git branch                 # 列出分支
git branch <name>          # 创建新分支
git checkout <branch>      # 切换分支
git checkout -b <branch>   # 创建并切换分支
git merge <branch>         # 合并分支
git branch -d <branch>     # 删除分支
```

### 4. 远程仓库 (Remote Repository)
```bash
git remote -v              # 查看远程仓库
git push origin <branch>   # 推送到远程仓库
git pull origin <branch>   # 从远程仓库拉取
git fetch                  # 获取远程更新
```

### 5. 历史记录 (History)
```bash
git log                    # 查看提交历史
git log --oneline          # 简洁历史记录
git show <commit>          # 查看特定提交
git reset <commit>         # 重置到特定提交
```

## 练习文件说明 (Practice Files Description)

本仓库包含以下练习文件:
- `examples/` - 示例文件目录
- `scripts/` - 脚本文件目录
- `.gitignore` - Git 忽略文件配置

## 学习建议 (Learning Tips)

1. 从基础命令开始练习
2. 尝试不同的分支操作
3. 练习解决合并冲突
4. 学习使用 .gitignore 文件
5. 理解 Git 的三个区域：工作区、暂存区、版本库
