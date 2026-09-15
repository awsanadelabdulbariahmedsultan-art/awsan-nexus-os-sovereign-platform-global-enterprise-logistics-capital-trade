from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any, Optional
import os

from backend.core.financial_engine import FinancialEngine
from backend.core.ai_agent import SovereignAIAgent
from backend.modules.ports_logistics import GlobalPortsEngine
from backend.modules.capital_markets_web3 import CapitalMarketsEngine
from backend.modules.edge_hardware_fleet import EdgeHardwareFleetEngine

# استيراد محرك الألعاب وتقنيات NVIDIA مع حماية من الأخطاء
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

# تفعيل CORS لتمكين عمل التطبيق والواجهة من أي متصفح أو هاتف أو كونسول
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

# نماذج طلبات أوامر الوكيل والتوسعات
class CopilotRequest(BaseModel):
    module: str
    prompt: str

class ExtensionRequest(BaseModel):
    module: str
    extension_name: str
    config: Optional[Dict[str, Any]] = None

# 1. الرابط الرئيسي (يفتح الداشبورد الملون التفاعلي وزر التثبيت)
@app.get("/")
def get_dashboard():
    if os.path.exists("frontend/dashboard.html"):
        return FileResponse("frontend/dashboard.html")
    elif os.path.exists("frontend/index.html"):
        return FileResponse("frontend/index.html")
    return {
        "system": "AWSAN NEXUS OS",
        "inventor": "Eng. Awsan Adel Sultan (01010305468)",
        "ai_engine": ai.model_engine,
        "hardware_layer": "Xreme Series & XG 100 Autonomous Enabled",
        "status": "ONLINE"
    }

# 2. ملفات التثبيت PWA لتنزيل التطبيق على الهاتف والكمبيوتر
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
        "edge_hardware_fleet": hardware_fleet.get_fleet_telemetry()
    }
    if gaming:
        data["gaming_and_nvidia"] = gaming.get_gaming_telemetry()
    return data

# 5. مسار تنفيذ أوامر الوكيل الذكي للبناء والتنفيذ
@app.post("/api/copilot/execute")
def execute_copilot(req: CopilotRequest):
    return ai.execute_builder(req.module, req.prompt)

# 6. مسار تسجيل وتفعيل التوسعات الديناميكية
@app.post("/api/extension/register")
def register_dynamic_extension(req: ExtensionRequest):
    return {
        "status": "EXTENSION_ATTACHED",
        "module": req.module,
        "extension": req.extension_name,
        "message": f"تمت إضافة التوسعة [{req.extension_name}] بنجاح إلى محور [{req.module}]."
    }
