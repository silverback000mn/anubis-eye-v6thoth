import numpy as np
from tensorflow.keras.models import load_model
from datetime import datetime

class BanPredictor:
    def __init__(self):
        self.model = load_model('ammit_model.h5')
        self.threshold = 0.87  # 87% de certeza para alerta

    def predict_ban_risk(self, account_data):
        """Analisa padrões para prever bans usando IA"""
        features = self._extract_features(account_data)
        risk_score = self.model.predict(np.array([features]))[0][0]
        
        return {
            "risk_level": "CRÍTICO" if risk_score > self.threshold else "ALERTA",
            "score": float(risk_score),
            "suggested_actions": self._get_recommendations(risk_score),
            "last_analysis": datetime.now().isoformat()
        }

    def _extract_features(self, data):
        return [
            data['actions_last_hour'] / 50,
            1 if data['proxy_rotation'] < 2 else 0,
            data['avg_session_minutes'] / 120
        ]

    def _get_recommendations(self, score):
        if score > 0.9:
            return ["PARAR IMEDIATAMENTE", "TROCAR PROXY", "REDUZIR ATIVIDADE EM 80%"]
        elif score > 0.8:
            return ["TROCAR PROXY", "PAUSAR POR 2H", "REVISAR PADRÕES"]
        else:
            return ["CONTINUAR MONITORANDO"]
