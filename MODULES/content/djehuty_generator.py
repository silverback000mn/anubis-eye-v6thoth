class SacredContent:
    def generate_bio(self):
        titles = ["Filho de Rá", "Sacerdote de Anúbis", "Guardião das Pirâmides"]
        return f"{random.choice(titles)} | Seguidor da Maat | #EgiptoSagrado"

    def create_post(self, theme):
        templates = {
            "templo": "✨ Luz divina no Templo de {location} hoje",
            "artefato": "🔮 Relíquia descoberta: {artifact_name}"
        }
        return templates.get(theme, "Bênçãos dos Deuses sobre vós")
