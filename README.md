## AdAnalyticsAPI ##

### Instalar Dependências e Atualizar Pacotes

Se o ambiente virtual já estiver configurado, você pode instalar ou atualizar as dependências necessárias com o seguinte comando:

```bash
pip install --upgrade -r requirements.txt
```


## 1. Endpoints de Usuários

## 1.1. `/docs`
**Método**: GET

**Resposta**:

**200 OK**: Retorna a documentação interativa da API, gerada pelo Swagger. Esta documentação exibe todos os endpoints disponíveis, seus parâmetros, tipos de resposta e exemplos de uso. É possível testar os endpoints diretamente na interface do Swagger, sem a necessidade de ferramentas externas.

## 1.2. `/instructions`
**Método**:  `GET`

**Resposta**:

**200 OK**: Retorna o conteúdo de um arquivo de texto com as instruções.

### 1.3. `/name`

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

## 2.2. `/<platform>/Resume`
**Método**: `GET`

**Descrição**: Recupera um resumo consolidado dos anúncios de uma plataforma específica. Esse endpoint retorna uma tabela agregada com somatório de valores numéricos e o nome da conta.

**Parâmetros**:

**platform** (string): O nome da plataforma de anúncios.
Resposta:

**200 OK**: Retorna os dados agregados da plataforma solicitada.
```json
[
  {
    "platform": "meta_ads",
    "account_name": "Account 1",
    "total_clicks": 30,
    "total_impressions": 5000,
    "total_cost": 150.00
  },
  {
    "platform": "google_ads",
    "account_name": "Account 2",
    "total_clicks": 25,
    "total_impressions": 4000,
    "total_cost": 120.00
  }
]
```

## 3. Endpoints Gerais
## 3.1. `/geral`
**Método**: `GET`

**Descrição**: Recupera os dados de todos os anúncios de todas as plataformas, agregados com as informações de cada plataforma e conta.

**Resposta**:

**200 OK**: Retorna todos os anúncios de todas as plataformas.
```json
[
  {
    "platform": "meta_ads",
    "ad_name": "Ad Example 1",
    "account_name": "Account 1",
    "clicks": 10,
    "impressions": 1000,
    "cost": 50.00
  },
  {
    "platform": "google_ads",
    "ad_name": "Ad Example 2",
    "account_name": "Account 2",
    "clicks": 20,
    "impressions": 1500,
    "cost": 70.00
  }
]
```

## 3.2. `/geral/resume`
**Método**: `GET`

**Descrição**: Recupera um resumo geral de todos os anúncios de todas as plataformas. As colunas numéricas são somadas, e as de texto são agregadas por plataforma.

**Resposta**:

**200 OK**: Retorna um resumo dos dados de todas as plataformas.

```json
[
  {
    "platform": "meta_ads",
    "total_clicks": 30,
    "total_impressions": 5000,
    "total_cost": 150.00
  },
  {
    "platform": "google_ads",
    "total_clicks": 25,
    "total_impressions": 4000,
    "total_cost": 120.00
  }
]
```

## Considerações Finais
A API permite acessar dados de várias plataformas de anúncios e oferece endpoints para consultar tanto dados individuais como agregados. Além disso, ela permite gerar resumos das informações e exportar os dados para arquivos CSV.

### Explicação:

1. **/docs**: Este endpoint retorna a documentação interativa da API gerada automaticamente pelo Swagger.
2. **/name**: Este endpoint retorna informações básicas do usuário, como nome, e-mail, LinkedIn e GitHub.
3. **/instructions**: Retorna um arquivo de texto com as instruções para acessar os dados da API.
4. **/{platform}**: Recupera dados dos anúncios de uma plataforma específica, identificada pelo nome fornecido na URL.
5. **/{platform}/Resume**: Retorna um resumo consolidado dos anúncios de uma plataforma específica.
6. **/geral**: Este endpoint retorna os dados de todos os anúncios de todas as plataformas.
7. **/geral/resumo**: Retorna um resumo geral com dados agregados de todas as plataformas.

Essa documentação fornece uma visão geral de como interagir com a API, descrevendo os parâmetros necessários e a estrutura de resposta para cada endpoint.
