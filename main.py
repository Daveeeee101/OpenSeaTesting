from datetime import datetime, timedelta

import GraphQLData
import requests

graphURL = "https://api.opensea.io/graphql/"

if __name__ == '__main__':
    header = GraphQLData.getHeader('OrdersQuery')
    body = GraphQLData.getQuery('OrdersQuery', makerArchetype={'assetContractAddress': "0x34d85c9cdeb23fa97cb08333b511ac86e1c4e258", 'tokenId': "65268", 'chain': "ETHEREUM"}, isValid=True)
    with requests.session() as s:
        rep = requests.post(url=graphURL, headers=header, data=body)
        print(rep.text)
