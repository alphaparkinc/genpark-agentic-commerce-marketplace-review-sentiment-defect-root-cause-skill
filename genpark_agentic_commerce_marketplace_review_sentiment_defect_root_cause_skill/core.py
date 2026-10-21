# -*- coding: utf-8 -*-
"""Marketplace Review NLP Defect Root Cause for GenPark Agentic Commerce."""
import json
from typing import Dict, Any, List

class ReviewNLPSentimentDefectRootCauseClassifier:
    @staticmethod
    def cluster_negative_review_defects(reviews: List[str]) -> Dict[str, Any]:
        clusters = {"HARDWARE_SNAPPING": 0, "BATTERY_DRAIN": 0, "PACKAGING_DAMAGE": 0, "SOFTWARE_FIRMWARE": 0}
        for r in reviews:
            text = r.lower()
            if "snap" in text or "broke" in text or "crack" in text: clusters["HARDWARE_SNAPPING"] += 1
            elif "battery" in text or "charge" in text: clusters["BATTERY_DRAIN"] += 1
            elif "box" in text or "dented" in text: clusters["PACKAGING_DAMAGE"] += 1
            else: clusters["SOFTWARE_FIRMWARE"] += 1
        return {"total_analyzed": len(reviews), "defect_clusters": clusters}

    @staticmethod
    def generate_factory_capa_report(defect_category: str, defect_rate_pct: float, sku: str) -> Dict[str, Any]:
        return {"sku": sku, "defect": defect_category, "rate": defect_rate_pct, "action": "MANDATE_BATCH_TENSILE_TESTING", "factory_remedy": "Thicken injection mold wall by 0.5mm."}
