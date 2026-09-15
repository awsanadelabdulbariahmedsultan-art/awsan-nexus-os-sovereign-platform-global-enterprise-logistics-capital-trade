#!/bin/bash
set -e

# ===========================================================================================
# AWSAN NEXUS OS (AN-OS) - Unified One-Click Launcher
# Author: Eng. Awsan Adel Abdulbari Ahmed Sultan (2026)
# ===========================================================================================

echo "=========================================================================="
echo "🚀 تشغيل منظومة AWSAN NEXUS OS السيادية (تثبيت الحزم + إطلاق الخادم)..."
echo "👤 المالك: Eng. Awsan Adel Abdulbari Ahmed Sultan (01010305468)"
echo "=========================================================================="

# 1. تنظيف أي مسافات خفية (U+00A0) داخل ملفات البايثون لضمان عدم حدوث أخطاء
python3 -c "import glob; [open(p,'w',encoding='utf-8').write(open(p,'r',encoding='utf-8').read().replace('\u00a0',' ')) for p in glob.glob('backend/**/*.py',recursive=True)]" 2>/dev/null || true

# 2. تثبيت الحزم المطلوبة تلقائياً
if [ -f "requirements.nexus.txt" ]; then
    echo "📦 جاري تثبيت وتحديث الحزم من requirements.nexus.txt..."
    pip install -r requirements.nexus.txt
elif [ -f "requirements.txt" ]; then
    echo "📦 جاري تثبيت الحزم من requirements.txt..."
    pip install -r requirements.txt
fi

# 3. إطلاق خادم المنصة المباشر وتفعيل منفذ 8000
echo "⚡ جاري إطلاق خادم المنظومة (FastAPI + Dashboard) على المنفذ 8000..."
python3 -m uvicorn backend.server:app --host 0.0.0.0 --port 8000 --reload
