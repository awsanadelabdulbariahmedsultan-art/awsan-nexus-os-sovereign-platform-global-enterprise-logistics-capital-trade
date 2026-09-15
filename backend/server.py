from fastapi import FastAPI
from fastapi.responses import HTMLResponse, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any, Optional

from backend.core.financial_engine import FinancialEngine
from backend.core.ai_agent import SovereignAIAgent
from backend.modules.ports_logistics import GlobalPortsEngine
from backend.modules.capital_markets_web3 import CapitalMarketsEngine
from backend.modules.edge_hardware_fleet import EdgeHardwareFleetEngine

try:
    from backend.modules.gaming_nvidia_engine import GamingNvidiaEngine
    gaming = GamingNvidiaEngine()
except Exception:
    gaming = None

app = FastAPI(
    title="AWSAN NEXUS OS Core",
    description="Sovereign Enterprise, Gaming & Universal PWA OS",
    version="2.5.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fin = FinancialEngine()
ai = SovereignAIAgent()
ports = GlobalPortsEngine()
markets = CapitalMarketsEngine()
hardware_fleet = EdgeHardwareFleetEngine()

# كود الواجهة الرسومية الملونة المدمج بالكامل لضمان عرضه 100%
DASHBOARD_HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AWSAN NEXUS OS (AN-OS) | Universal Dashboard</title>
    <link rel="manifest" href="/manifest.json">
    <meta name="theme-color" content="#2563eb">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        body { font-family: system-ui, -apple-system, sans-serif; background-color: #030712; color: #f3f4f6; }
        .glass-card { background: rgba(17, 24, 39, 0.9); backdrop-filter: blur(12px); border: 1px solid rgba(75, 85, 99, 0.4); }
    </style>
</head>
<body class="min-h-screen p-6">
    <header class="max-w-7xl mx-auto flex flex-wrap justify-between items-center border-b border-gray-800 pb-5 mb-6 gap-4">
        <div>
            <h1 class="text-2xl font-black text-blue-400 flex items-center">
                <i class="fa-solid fa-satellite-dish ml-2 text-cyan-400"></i> AWSAN NEXUS OS 
                <span class="text-xs bg-blue-900/80 text-blue-300 px-2 py-0.5 rounded mr-2 border border-blue-600">Universal v2.5 Live</span>
            </h1>
            <p class="text-xs text-gray-400 mt-1">Eng. Awsan Adel Abdulbari Ahmed Sultan | Yemen (ID: 01010305468)</p>
        </div>
        
        <div class="flex items-center space-x-2 space-x-reverse flex-wrap gap-2">
            <!-- زر التثبيت PWA المباشر على الهاتف والكمبيوتر -->
            <button id="pwaInstallBtn" onclick="installAppDirectly()" class="px-4 py-2 bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white rounded-lg text-xs font-bold shadow-lg transition flex items-center animate-pulse">
                <i class="fa-solid fa-download ml-2"></i> 📲 تثبيت التطبيق على جهازك (Install App)
            </button>
            <span class="px-3 py-1 bg-green-950 border border-green-700 text-green-400 text-xs rounded-full">
                <i class="fa-brands fa-nvidia ml-1"></i> NVIDIA Omniverse + ACE
            </span>
            <span class="px-3 py-1 bg-purple-950 border border-purple-700 text-purple-400 text-xs rounded-full">
                <i class="fa-brands fa-playstation ml-1"></i> PS5 / <i class="fa-brands fa-xbox mx-1"></i> Xbox
            </span>
            <span class="px-3 py-1 bg-emerald-950 border border-emerald-700 text-emerald-400 text-xs rounded-full">
                ● متصل عالمياً
            </span>
        </div>
    </header>

    <!-- شريط التوافقية مع المتاجر والأنظمة -->
    <div class="max-w-7xl mx-auto mb-6 p-4 glass-card rounded-xl flex flex-wrap items-center justify-between gap-4">
        <div class="text-xs text-gray-300">
            <span class="font-bold text-blue-400"><i class="fa-solid fa-mobile-screen ml-1"></i> متاح للتحميل والتثبيت:</span>
            <span>يدعم التثبيت المباشر كـ App لهواتف Android وحواسيب Mac و Windows وشاشات الكونسول.</span>
        </div>
        <div class="flex items-center space-x-2 space-x-reverse text-xs">
            <span class="px-2.5 py-1 rounded bg-gray-800 border border-gray-700 text-gray-300"><i class="fa-brands fa-google-play ml-1 text-emerald-400"></i> Google Play Ready</span>
            <span class="px-2.5 py-1 rounded bg-gray-800 border border-gray-700 text-gray-300"><i class="fa-brands fa-windows ml-1 text-blue-400"></i> Windows Store</span>
            <span class="px-2.5 py-1 rounded bg-gray-800 border border-gray-700 text-gray-300"><i class="fa-brands fa-apple ml-1 text-gray-200"></i> macOS App</span>
        </div>
    </div>

    <!-- شبكة المحاور الأربعة الرئيسية -->
    <main class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-6">
        <div class="glass-card p-5 rounded-xl border-l-4 border-l-blue-500">
            <div class="flex justify-between items-center text-xs text-blue-400">
                <span class="font-bold">النظام المالي الصارم</span>
                <span class="bg-blue-900/60 px-2 py-0.5 rounded">[+] توسعة</span>
            </div>
            <div class="text-2xl font-black mt-2 text-white">$268,500.00</div>
            <p class="text-[11px] text-emerald-400 mt-2"><i class="fa-solid fa-shield-halved ml-1"></i> حظر الترحيل دون إذن (94 نموذجاً)</p>
        </div>

        <div class="glass-card p-5 rounded-xl border-l-4 border-l-cyan-500">
            <div class="flex justify-between items-center text-xs text-cyan-400">
                <span class="font-bold">موانئ العالم واللوجستيات</span>
                <span class="bg-cyan-900/60 px-2 py-0.5 rounded">[🤖 AI] وكيل</span>
            </div>
            <div class="text-2xl font-black mt-2 text-white">6 موانئ نشطة</div>
            <p class="text-[11px] text-cyan-400 mt-2"><i class="fa-solid fa-ship ml-1"></i> AIS تتبع راداري لعدن والحديدة وروتردام</p>
        </div>

        <div class="glass-card p-5 rounded-xl border-l-4 border-l-green-500">
            <div class="flex justify-between items-center text-xs text-green-400">
                <span class="font-bold">محرك NVIDIA ACE & 3D</span>
                <span class="bg-green-900/60 px-2 py-0.5 rounded">[RTX]</span>
            </div>
            <div class="text-2xl font-black mt-2 text-white">Omniverse Live</div>
            <p class="text-[11px] text-green-400 mt-2"><i class="fa-solid fa-cube ml-1"></i> توأم رقمي تفاعلي للموانئ ومناجم مأرب</p>
        </div>

        <div class="glass-card p-5 rounded-xl border-l-4 border-l-purple-500">
            <div class="flex justify-between items-center text-xs text-purple-400">
                <span class="font-bold">أجهزة الألعاب والكونسول</span>
                <span class="bg-purple-900/60 px-2 py-0.5 rounded"><i class="fa-solid fa-gamepad"></i></span>
            </div>
            <div class="text-2xl font-black mt-2 text-white">DualSense & Xbox</div>
            <p class="text-[11px] text-purple-400 mt-2" id="controller-status"><i class="fa-solid fa-circle-check ml-1"></i> جاهز للتحكم بذراع الألعاب</p>
        </div>
    </main>

    <!-- روابط الوصول السريع للخدمات -->
    <div class="max-w-7xl mx-auto mt-8 flex flex-wrap justify-between items-center gap-4 pt-4 border-t border-gray-800 text-xs text-gray-400">
        <div>
            <span>الحالة التشغيلية: </span>
            <span class="text-emerald-400 font-bold">ONLINE (Quinn-3.8 Engine)</span>
        </div>
        <div class="space-x-4 space-x-reverse">
            <a href="/api/overview" class="hover:text-blue-400 underline">المؤشرات الحية (/api/overview)</a>
            <a href="/api/system" class="hover:text-blue-400 underline">بيانات السيادة (/api/system)</a>
            <a href="/docs" class="hover:text-blue-400 underline">بوابة الـ API (/docs)</a>
        </div>
    </div>

    <script>
        if ('serviceWorker' in navigator) {
            navigator.serviceWorker.register('/sw.js').then(() => console.log('SW Ready'));
        }

        let deferredPrompt;
        window.addEventListener('beforeinstallprompt', (e) => {
            e.preventDefault();
            deferredPrompt = e;
        });

        function installAppDirectly() {
            if (deferredPrompt) {
                deferredPrompt.prompt();
                deferredPrompt = null;
            } else {
                alert("لتثبيت التطبيق على هاتفك: اضغط على خيارات المتصفح (⋮) في أعلى الشاشة واختر 'تثبيت التطبيق' أو 'إضافة إلى الشاشة الرئيسية'.");
            }
        }

        window.addEventListener("gamepadconnected", (e) => {
            document.getElementById("controller-status").innerHTML = "🎮 متصل: " + e.gamepad.id.substring(0, 18);
        });
    </script>
</body>
</html>
"""

# 1. الرابط الرئيسي يعرض الواجهة الرسومية الملونة فوراً دون أي اعتمادية
@app.get("/", response_class=HTMLResponse)
def get_dashboard():
    return HTMLResponse(content=DASHBOARD_HTML)

# 2. ملف تعريف التطبيق PWA للتثبيت المباشر
@app.get("/manifest.json")
def get_manifest():
    manifest_content = """{
      "name": "AWSAN NEXUS OS",
      "short_name": "NexusOS",
      "start_url": "/",
      "display": "standalone",
      "background_color": "#030712",
      "theme_color": "#2563eb",
      "icons": [
        {
          "src": "https://cdn-icons-png.flaticon.com/512/9068/9068779.png",
          "sizes": "512x512",
          "type": "image/png"
        }
      ]
    }"""
    return Response(content=manifest_content, media_type="application/manifest+json")

# 3. عامل الخدمة PWA
@app.get("/sw.js")
def get_sw():
    sw_content = """
    self.addEventListener('install', (e) => { self.skipWaiting(); });
    self.addEventListener('fetch', (e) => { e.respondWith(fetch(e.request)); });
    """
    return Response(content=sw_content, media_type="application/javascript")

# 4. مسار بيانات السيادة وحالة النظام (JSON)
@app.get("/api/system")
def get_system_status():
    return {
        "system": "AWSAN NEXUS OS",
        "inventor": "Eng. Awsan Adel Sultan (01010305468)",
        "ai_engine": ai.model_engine,
        "hardware_layer": "Xreme Series & XG 100 Autonomous Enabled",
        "status": "ONLINE"
    }

# 5. مسار المؤشرات الشاملة
@app.get("/api/overview")
def overview():
    stats = fin.get_stats()
    data = {
        "financials": stats,
        "ai_intelligence": ai.audit_and_advise(stats),
        "ports_network": ports.get_ports(),
        "market_and_mining": markets.get_market_telemetry(),
        "edge_hardware_fleet": hardware_fleet.get_fleet_telemetry()
    }
    if gaming:
        data["gaming_and_nvidia"] = gaming.get_gaming_telemetry()
    return data
