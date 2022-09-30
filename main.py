import GraphQLData
import requests

graphURL = "https://api.opensea.io/graphql/"

if __name__ == '__main__':
    header = GraphQLData.getHeader('EventHistoryPollQuery')
    body = GraphQLData.getQuery('EventHistoryPollQuery', archetype=None,
                                collections=['dodoor-nft'], chains=[],
                                eventTypes=['CREATED', 'SUCCESSFUL', 'CANCELLED'])
    with requests.session() as s:
        rep = requests.post(graphURL, headers=header, data=body)
