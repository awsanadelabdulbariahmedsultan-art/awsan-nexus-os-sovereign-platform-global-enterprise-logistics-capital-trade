from fastapi import FastAPI
from backend.core.financial_engine import FinancialEngine
from backend.core.ai_agent import SovereignAIAgent
from backend.modules.ports_logistics import GlobalPortsEngine
from backend.modules.capital_markets_web3 import CapitalMarketsEngine
from backend.modules.edge_hardware_fleet import EdgeHardwareFleetEngine

app = FastAPI(
    title="AWSAN NEXUS OS Core",
    description="Sovereign Enterprise OS Powered by Quinn-3.8 and Autonomous Edge Hardware"
)

fin = FinancialEngine()
ai = SovereignAIAgent()
ports = GlobalPortsEngine()
markets = CapitalMarketsEngine()
hardware_fleet = EdgeHardwareFleetEngine()

@app.get("/")
def root():
    return {
        "system": "AWSAN NEXUS OS",
        "inventor": "Eng. Awsan Adel Sultan (01010305468)",
        "ai_engine": ai.model_engine,
        "hardware_layer": "Xreme Series & XG 100 Autonomous Enabled",
        "status": "ONLINE"
    }

@app.get("/api/overview")
def overview():
    stats = fin.get_stats()
    return {
        "financials": stats,
        "ai_intelligence": ai.audit_and_advise(stats),
        "ports_network": ports.get_ports(),
        "market_and_mining": markets.get_market_telemetry(),
        "edge_hardware_fleet": hardware_fleet.get_fleet_telemetry()
    }
