from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

from backend.core.financial_engine import FinancialEngine
from backend.core.ai_agent import SovereignAIAgent
from backend.modules.ports_logistics import GlobalPortsEngine
from backend.modules.capital_markets_web3 import CapitalMarketsEngine
from backend.modules.edge_hardware_fleet import EdgeHardwareFleetEngine

# استيراد محرك الألعاب وNVIDIA مع حماية من الأخطاء
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

fin = FinancialEngine()
ai = SovereignAIAgent()
ports = GlobalPortsEngine()
markets = CapitalMarketsEngine()
hardware_fleet = EdgeHardwareFleetEngine()

# 1. الرابط الرئيسي (يفتح واجهة dashboard.html التفاعلية وزر التثبيت)
@app.get("/")
def get_dashboard():
    if os.path.exists("frontend/dashboard.html"):
        return FileResponse("frontend/dashboard.html")
    elif os.path.exists("frontend/index.html"):
        return FileResponse("frontend/index.html")
    # في حال عدم العثور على ملف الواجهة، يعرض حالة النظام البرمجية تلقائياً
    return {
        "system": "AWSAN NEXUS OS",
        "inventor": "Eng. Awsan Adel Sultan (01010305468)",
        "ai_engine": ai.model_engine,
        "hardware_layer": "Xreme Series & XG 100 Autonomous Enabled",
        "status": "ONLINE"
    }

# 2. ملفات التثبيت الفوري كـ App على الهاتف والكمبيوتر (PWA)
@app.get("/manifest.json")
def get_manifest():
    return FileResponse("frontend/manifest.json", media_type="application/manifest+json")

@app.get("/sw.js")
def get_sw():
    return FileResponse("frontend/sw.js", media_type="application/javascript")

# 3. مسار بيانات السيادة وحالة النظام البرمجية
@app.get("/api/system")
def get_system_status():
    return {
        "system": "AWSAN NEXUS OS",
        "inventor": "Eng. Awsan Adel Sultan (01010305468)",
        "ai_engine": ai.model_engine,
        "hardware_layer": "Xreme Series & XG 100 Autonomous Enabled",
        "status": "ONLINE"
    }

# 4. مسار المؤشرات الشاملة (المالية، الموانئ، الأسواق، الأساطيل، والألعاب)
@app.get("/api/overview")
def get_overview():
    stats = fin.get_stats()
    data = {
        "financials": stats,
        "ai_intelligence": ai.audit_and_advise(stats),
        "ports_network": ports.get_ports(),
        "market_and_mining": markets.get_market_telemetry(),
        "hardware_fleets": hardware_fleet.get_fleet_telemetry()
    }
    if gaming:
        data["gaming_and_nvidia"] = gaming.get_gaming_telemetry()
    return data
