from datetime import datetime, timedelta

import GraphQLData
import requests

graphURL = "https://api.opensea.io/graphql/"

if __name__ == '__main__':
    header = GraphQLData.getHeader('OrdersQuery')
    body = GraphQLData.getQuery('OrdersQuery', )
    with requests.session() as s:
        rep = requests.post(url=graphURL, headers=header, data=body)
        print(rep.text)
