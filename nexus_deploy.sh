#!/bin/bash
set -e

# ===========================================================================================
# OFFICIAL INTELLECTUAL PROPERTY & IMPLEMENTATION RIGHTS RESERVED © 2026
# PROJECT: AWSAN NEXUS OS (AN-OS) - Autonomous Global Enterprise, Gaming & Trade Platform
# INVENTOR: Eng. Awsan Adel Abdulbari Ahmed Sultan
# NATIONAL ID: 01010305468 | REPUBLIC OF YEMEN
# CONTACT: +967 777852433 / +967 7776633003 | EMAIL: awsandew@outlook.com
# ===========================================================================================

REPO_NAME="awsan-nexus-os-sovereign-platform-global-enterprise-logistics-capital-trade"
GITHUB_TOKEN="${GITHUB_TOKEN:-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}"
GITHUB_USER="awsanadelabdulbariahmedsultan-art"

echo "=========================================================================="
echo "🚀 تشغيل سكربت التحديث السيادي الموحد (nexus_deploy.sh)..."
echo "👤 المالك: Eng. Awsan Adel Abdulbari Ahmed Sultan (01010305468)"
echo "=========================================================================="

mkdir -p backend/{core,modules} frontend docs

# 1. تنظيف أي مسافات خفية (U+00A0) داخل ملفات البايثون
python3 -c "import glob; [open(p,'w',encoding='utf-8').write(open(p,'r',encoding='utf-8').read().replace('\u00a0',' ')) for p in glob.glob('backend/**/*.py',recursive=True)]" 2>/dev/null || true

# 2. توليد وتحديث البصمة الرقمية المشفرة SHA-256
sha256sum backend/server.py backend/core/financial_engine.py docs/SOVEREIGN_IP_NOTICE.txt > docs/DIGITAL_SIGNATURE_SHA256.txt 2>/dev/null || true

# 3. إعداد مستودع Git وحفظ التحديثات والرفع التلقائي إلى GitHub
git config user.name "Eng. Awsan Adel Abdulbari Ahmed Sultan"
git config user.email "awsandew@outlook.com"
git add .
git commit -m "Update Core: Use Dockerfile.nexus, server.py and dashboard.html" || true
git branch -M main
git remote remove origin 2>/dev/null || true
git remote add origin "https://${GITHUB_TOKEN}@github.com/${GITHUB_USER}/${REPO_NAME}.git"

echo "📤 جاري الرفع التلقائي إلى مستودع GitHub..."
git push -u origin main --force

echo "=========================================================================="
echo "✅ تم تحديث ورفع كافة ملفات المنظومة بنجاح!"
echo "🔗 رابط المستودع: https://github.com/${GITHUB_USER}/${REPO_NAME}"
echo "=========================================================================="
