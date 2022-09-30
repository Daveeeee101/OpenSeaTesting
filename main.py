import GraphQLData
import requests

graphURL = "https://api.opensea.io/graphql/"

if __name__ == '__main__':
    header = GraphQLData.getHeader('EventHistoryPollQuery')
    body = GraphQLData.getQuery('EventHistoryPollQuery', archetype=None,
                                collections=['dodoor-nft'], chains=[],
                                eventTypes=['AUCTION_CREATED', 'AUCTION_SUCCESSFUL', 'AUCTION_CANCELLED'])
    with requests.session() as s:
        rep = requests.post(url=graphURL, headers=header, data=body)
        print(rep.text)
