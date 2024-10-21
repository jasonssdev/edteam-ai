import requests
import os
import certifi

# Usar el archivo de certificados
os.environ['SSL_CERT_FILE'] = certifi.where()

# Intentar realizar una solicitud
response = requests.get("https://api.openai.com")
print(response.status_code)
