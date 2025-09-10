# Git 练习任务 (Git Practice Tasks)

## 任务列表 (Task List)

### 基础任务 (Basic Tasks)
- [ ] 修改 README.md 文件
- [ ] 添加新的示例文件
- [ ] 创建并切换到新分支
- [ ] 在新分支中进行修改
- [ ] 将更改合并回主分支

### 中级任务 (Intermediate Tasks)
- [ ] 创建多个分支并进行不同修改
- [ ] 练习解决合并冲突
- [ ] 使用 git stash 保存临时更改
- [ ] 使用 git revert 撤销提交
- [ ] 使用 git reset 回退版本

### 高级任务 (Advanced Tasks)
- [ ] 使用 git rebase 整理提交历史
- [ ] 创建和应用 git patch
- [ ] 使用 git cherry-pick 选择性合并
- [ ] 配置 git hooks
- [ ] 使用 git worktree 管理多个工作目录

## 练习记录 (Practice Log)

请在完成每个任务后在此记录：

```
日期: ____
完成任务: ____
学到的内容: ____
遇到的问题: ____
解决方案: ____
```

## 有用的 Git 命令速查 (Quick Git Commands Reference)

```bash
# 查看帮助
git help <command>

# 查看配置
git config --list

# 查看远程仓库详情
git remote show origin

# 查看文件更改历史
git log --follow <file>

# 查看谁修改了某行代码
git blame <file>

# 搜索提交信息
git log --grep="关键词"

# 查看两个提交之间的差异
git diff <commit1>..<commit2>
```