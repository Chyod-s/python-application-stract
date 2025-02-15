## python-application-stract ##

### Instalar Dependências e Atualizar Pacotes

Se você já tem o ambiente virtual configurado e as dependências instaladas, pode atualizar todos os pacotes para as versões mais recentes com o seguinte comando:

```bash
pip install --upgrade -r requirements.txt
```


## 1. Endpoints de Usuários

## 1.1. `/instructions`
**Método**:  `GET`

**Resposta**:

**200 OK**: Retorna o conteúdo de um arquivo de texto com as instruções.

### 1.2. `/nome`

**Método**: `GET`

**Descrição**: Retorna as informações do usuário, como nome, e-mail, LinkedIn e GitHub.

**Resposta**:
- **200 OK**: Retorna um dicionário contendo as informações do usuário.
  ```json
  {
    "name": "Klayton",
    "email": "klayton@example.com",
    "linkedIn": "https://www.linkedin.com/in/klayton",
    "github": "https://github.com/klayton"
  }

## 2. Endpoints de Anúncios
## 2.1. `/<platform>`
**Método:** `GET`

**Descrição**: Recupera os dados de anúncios de uma plataforma específica. O parâmetro <platform> é o nome da plataforma de anúncios, como meta_ads ou google_ads.

**Parâmetros**:

**platform** (string): O nome da plataforma de anúncios.

**Resposta**:

**200 OK**: Retorna os dados de anúncios da plataforma solicitada.
```json
[
  {
    "ad_name": "Ad Example 1",
    "clicks": 10,
    "impressions": 1000,
    "cost": 50.00
  },
  {
    "ad_name": "Ad Example 2",
    "clicks": 20,
    "impressions": 1500,
    "cost": 70.00
  }
]
```

