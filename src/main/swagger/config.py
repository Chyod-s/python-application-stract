from flask_restx import Api

api = Api(title='AdAnalyticsAPI', version='1.0', description='Flask API that fetches data from an external platform and provides real-time reports via RESTful endpoints in JSON and CSV format.', doc="/docs")