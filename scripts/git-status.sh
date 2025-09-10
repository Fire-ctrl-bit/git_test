#!/bin/bash

# Git 学习辅助脚本
# Git Learning Helper Script

echo "=== Git 学习辅助脚本 ==="
echo ""

# 显示当前仓库状态
echo "📊 当前仓库状态 (Current Repository Status):"
git status --short

echo ""

# 显示最近的提交
echo "📝 最近的提交 (Recent Commits):"
git log --oneline -5

echo ""

# 显示分支信息
echo "🌿 分支信息 (Branch Information):"
git branch -v

echo ""

# 显示远程仓库
echo "🌐 远程仓库 (Remote Repositories):"
git remote -v

echo ""
echo "✅ 状态检查完成！"