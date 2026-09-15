"""
AWSAN NEXUS OS - Global & National Maritime Ports AIS Engine
Yemeni Sovereign Ports, Regional Maritime Hubs & Worldwide Port Terminals
Author: Eng. Awsan Adel Abdulbari Ahmed Sultan (2026)
"""
from typing import List, Dict, Any

class GlobalPortsEngine:
    def __init__(self):
        # 1. الموانئ البحرية اليمنية السيادية (12 ميناء)
        self.yemeni_ports = [
            {"code": "YE-ADE", "name": "ميناء عدن الدولي للحاويات", "province": "عدن", "type": "حاويات وتجاري رئيسي", "status": "ACTIVE", "occupancy": "68%"},
            {"code": "YE-HOD", "name": "ميناء الحديدة الحيوي", "province": "الحديدة", "type": "حاويات وبضائع عامة", "status": "ACTIVE", "occupancy": "62%"},
            {"code": "YE-MOK", "name": "ميناء المخا التاريخي الاستراتيجي", "province": "تعز / باب المندب", "type": "تجاري وملاحة استراتيجية", "status": "EXPANDING", "occupancy": "45%"},
            {"code": "YE-SAL", "name": "ميناء الصليف البحري", "province": "الحديدة", "type": "استقبال الحبوب والصب الجاف", "status": "ACTIVE", "occupancy": "54%"},
            {"code": "YE-MKX", "name": "ميناء المكلا الدولي", "province": "حضرموت", "type": "تجاري وحاويات", "status": "ACTIVE", "occupancy": "58%"},
            {"code": "YE-ASH", "name": "ميناء الشحر والضبة النفطي", "province": "حضرموت", "type": "تصدير النفط الخام والصب السائل", "status": "MONITORED", "occupancy": "70%"},
            {"code": "YE-NIS", "name": "ميناء نشطون الساحلي", "province": "المهرة", "type": "شحن وتجارة المهرة وسلطنة عمان", "status": "ACTIVE", "occupancy": "40%"},
            {"code": "YE-QAN", "name": "ميناء قنا والنشيمة", "province": "شبوة", "type": "تصدير المشتقات والنفط", "status": "ACTIVE", "occupancy": "50%"},
            {"code": "YE-BAL", "name": "ميناء بلحاف الاستراتيجي للغاز المسال", "province": "شبوة", "type": "تصدير الغاز الطبيعي المسال LNG", "status": "SECURED", "occupancy": "75%"},
            {"code": "YE-SCT", "name": "ميناء حولاف - سقطرى", "province": "أرخبيل سقطرى", "type": "شريان أرخبيل سقطرى البحري", "status": "ACTIVE", "occupancy": "35%"},
            {"code": "YE-RAI", "name": "ميناء رأس عيسى البحري", "province": "الحديدة", "type": "تخزين وتصدير المشتقات", "status": "MONITORED", "occupancy": "60%"},
            {"code": "YE-DHU", "name": "مرسى ذباب وباب المندب", "province": "تعز / المضيق الدولي", "type": "مراقبة الممر الملاحي الدولي", "status": "STRATEGIC_ACTIVE", "occupancy": "80%"}
        ]

        # 2. الموانئ الإقليمية الكبرى (السعودية، الإمارات، مصر، عمان)
        self.regional_ports = [
            {"code": "SA-JED", "name": "ميناء جدة الإسلامي", "country": "المملكة العربية السعودية", "status": "OPTIMAL", "occupancy": "74%"},
            {"code": "SA-DMM", "name": "ميناء الملك عبدالعزيز بالدمام", "country": "المملكة العربية السعودية", "status": "OPTIMAL", "occupancy": "71%"},
            {"code": "SA-KAP", "name": "ميناء الملك عبدالله - رابغ", "country": "المملكة العربية السعودية", "status": "OPTIMAL", "occupancy": "65%"},
            {"code": "SA-JAZ", "name": "ميناء جازان الإقليمي", "country": "المملكة العربية السعودية", "status": "ACTIVE", "occupancy": "58%"},
            {"code": "AE-JEA", "name": "ميناء جبل علي - دبي", "country": "دولة الإمارات العربية المتحدة", "status": "HIGH_THROUGHPUT", "occupancy": "86%"},
            {"code": "AE-KHL", "name": "ميناء خليفة - أبوظبي", "country": "دولة الإمارات العربية المتحدة", "status": "OPTIMAL", "occupancy": "73%"},
            {"code": "AE-FUJ", "name": "ميناء الفجيرة العالمي للوقود", "country": "دولة الإمارات العربية المتحدة", "status": "OPTIMAL", "occupancy": "82%"},
            {"code": "EG-PSD", "name": "ميناء شرق بورسعيد وقناة السويس", "country": "جمهورية مصر العربية", "status": "HIGH_THROUGHPUT", "occupancy": "88%"},
            {"code": "EG-AIS", "name": "ميناء العين السخنة", "country": "جمهورية مصر العربية", "status": "ACTIVE", "occupancy": "69%"},
            {"code": "EG-ALY", "name": "ميناء الإسكندرية البحري", "country": "جمهورية مصر العربية", "status": "ACTIVE", "occupancy": "76%"},
            {"code": "OM-SLL", "name": "ميناء صلالة الاستراتيجي", "country": "سلطنة عمان", "status": "OPTIMAL", "occupancy": "70%"},
            {"code": "OM-DQM", "name": "ميناء الدقم الصناعي", "country": "سلطنة عمان", "status": "ACTIVE", "occupancy": "52%"},
            {"code": "OM-SOH", "name": "ميناء صحار التجاري", "country": "سلطنة عمان", "status": "OPTIMAL", "occupancy": "67%"}
        ]

        # 3. الموانئ الدولية الكبرى (الصين، الهند، إيران، أمريكا، روسيا، أوروبا)
        self.international_ports = [
            {"code": "CN-SHA", "name": "ميناء شنغهاي الدولي (الأكبر عالمياً)", "country": "الصين", "status": "MAX_CAPACITY", "occupancy": "94%"},
            {"code": "CN-NGB", "name": "ميناء نينغبو-تشوشان", "country": "الصين", "status": "OPTIMAL", "occupancy": "89%"},
            {"code": "CN-SZX", "name": "ميناء شنجن المتطور", "country": "الصين", "status": "OPTIMAL", "occupancy": "87%"},
            {"code": "IN-NSA", "name": "ميناء جواهر لال نهرو (JNPT مومباي)", "country": "الهند", "status": "OPTIMAL", "occupancy": "81%"},
            {"code": "IN-MUN", "name": "ميناء موندرا الضخم - كجرات", "country": "الهند", "status": "ACTIVE", "occupancy": "78%"},
            {"code": "IR-BND", "name": "ميناء الشهيد رجائي - بندر عباس", "country": "إيران", "status": "ACTIVE", "occupancy": "75%"},
            {"code": "IR-ZBR", "name": "ميناء تشابهار الاستراتيجي", "country": "إيران", "status": "ACTIVE", "occupancy": "60%"},
            {"code": "US-LAX", "name": "ميناء لوس أنجلوس", "country": "الولايات المتحدة", "status": "HIGH_TRAFFIC", "occupancy": "88%"},
            {"code": "US-HOU", "name": "ميناء هيوستن للطاقة والكيماويات", "country": "الولايات المتحدة", "status": "OPTIMAL", "occupancy": "83%"},
            {"code": "RU-NVS", "name": "ميناء نوفوروسيسك - البحر الأسود", "country": "روسيا", "status": "ACTIVE", "occupancy": "79%"},
            {"code": "RU-VVO", "name": "ميناء فلاديفوستوك - المحيط الهادئ", "country": "روسيا", "status": "ACTIVE", "occupancy": "72%"},
            {"code": "NL-RTM", "name": "ميناء روتردام (بوابة أوروبا الرئيسية)", "country": "هولندا / أوروبا", "status": "OPTIMAL", "occupancy": "85%"},
            {"code": "BE-ANR", "name": "ميناء أنتويرب-بروج", "country": "بلجيكا / أوروبا", "status": "OPTIMAL", "occupancy": "82%"},
            {"code": "DE-HAM", "name": "ميناء هامبورغ", "country": "ألمانيا / أوروبا", "status": "OPTIMAL", "occupancy": "77%"},
            {"code": "ES-ALG", "name": "ميناء الجزيرة الخضراء", "country": "إسبانيا / أوروبا", "status": "OPTIMAL", "occupancy": "80%"}
        ]

    def get_ports(self) -> Dict[str, Any]:
        return {
            "summary": {
                "total_monitored_ports": len(self.yemeni_ports) + len(self.regional_ports) + len(self.international_ports),
                "yemen_ports_count": len(self.yemeni_ports),
                "regional_ports_count": len(self.regional_ports),
                "international_ports_count": len(self.international_ports),
                "ais_satellite_tracking": "ONLINE_ACTIVE_24_7"
            },
            "yemen_strategic_ports": self.yemeni_ports,
            "regional_maritime_hubs": self.regional_ports,
            "international_global_ports": self.international_ports
        }

    def simulate_vessel_voyage(self, vessel_name: str, origin_code: str, dest_code: str) -> Dict[str, Any]:
        return {
            "vessel_name": vessel_name,
            "origin_port": origin_code,
            "destination_port": dest_code,
            "navigation_status": "UNDERWAY_OPTIMAL_SPEED",
            "chokepoint_monitoring": "BAB_AL_MANDAB_SECURE",
            "ais_telemetry": "CONNECTED_SATELLITE",
            "eta_hours": 36.5
        }
