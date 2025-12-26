from service.service import Service

yahoo_service = Service('https://fantasysports.yahooapis.com/fantasy/v2')

def get_leagues(token: str):
    return yahoo_service.post('/league', headers={
        'Authorization': f'Bearer {token}'
    })