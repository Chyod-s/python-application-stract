from flask_restx import Api

desc = """
A AdAnalyticsAPI é uma API desenvolvida em Python com Flask, projetada para buscar dados de plataformas externas e fornecer relatórios analíticos em tempo real. A API oferece endpoints RESTful acessíveis via GET na raiz do localhost, com suporte para resposta em formatos JSON e CSV. Focada em simplicidade e desempenho, a API permite a agregação de dados analíticos com o mínimo de dependências, fornecendo insights valiosos de maneira eficiente.
"""

api = Api(title='AdAnalyticsAPI', version='1.0', description=desc, doc="/docs")