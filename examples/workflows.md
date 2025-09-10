# Git 工作流程示例 (Git Workflow Examples)

## 基础工作流程 (Basic Workflow)

### 1. 日常开发流程
```bash
# 1. 创建新分支
git checkout -b feature/new-feature

# 2. 进行开发工作
echo "新功能代码" > new-feature.txt

# 3. 添加文件到暂存区
git add new-feature.txt

# 4. 提交更改
git commit -m "添加新功能"

# 5. 推送到远程仓库
git push origin feature/new-feature
```

### 2. 合并工作流程
```bash
# 1. 切换到主分支
git checkout main

# 2. 更新主分支
git pull origin main

# 3. 合并功能分支
git merge feature/new-feature

# 4. 推送合并结果
git push origin main

# 5. 删除功能分支
git branch -d feature/new-feature
```

### 3. 解决冲突
```bash
# 当合并出现冲突时：
# 1. 查看冲突文件
git status

# 2. 编辑冲突文件，解决冲突标记
# <<<<<<< HEAD
# 当前分支的内容
# =======
# 要合并分支的内容
# >>>>>>> branch-name

# 3. 标记冲突已解决
git add <冲突文件>

# 4. 完成合并
git commit
```

## 实验建议 (Practice Suggestions)

1. 在此仓库中创建新分支练习
2. 修改不同文件并练习合并
3. 故意创建冲突并练习解决
4. 使用不同的合并策略