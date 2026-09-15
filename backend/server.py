from fastapi import FastAPI
from fastapi.responses import FileResponse
from backend.core.financial_engine import FinancialEngine
from backend.core.ai_agent import SovereignAIAgent
from backend.modules.ports_logistics import GlobalPortsEngine
from backend.modules.capital_markets_web3 import CapitalMarketsEngine
from backend.modules.edge_hardware_fleet import EdgeHardwareFleetEngine
from backend.modules.gaming_nvidia_engine import GamingNvidiaEngine

app = FastAPI(
    title="AWSAN NEXUS OS Core",
    description="Sovereign Enterprise, Gaming & Universal PWA OS",
    version="2.5.0"
)

fin = FinancialEngine()
ai = SovereignAIAgent()
ports = GlobalPortsEngine()
markets = CapitalMarketsEngine()
hardware = EdgeHardwareFleetEngine()
gaming = GamingNvidiaEngine()

# تقديم واجهة لوحة التحكم وملفات التثبيت PWA
@app.get("/")
def get_dashboard():
    return FileResponse("frontend/dashboard.html")

@app.get("/manifest.json")
def get_manifest():
    return FileResponse("frontend/manifest.json", media_type="application/manifest+json")

@app.get("/sw.js")
def get_sw():
    return FileResponse("frontend/sw.js", media_type="application/javascript")

@app.get("/api/overview")
def get_overview():
    stats = fin.get_stats()
    return {
        "financials": stats,
        "ai": ai.audit_and_advise(stats),
        "ports": ports.get_ports(),
        "markets": markets.get_market_telemetry(),
        "hardware_fleets": hardware.get_fleet_telemetry(),
        "gaming_and_nvidia": gaming.get_gaming_telemetry()
    }
