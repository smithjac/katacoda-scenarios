from ghapi.all import GhApi
import wonderwords
import dotenv
import os

dotenv.load_dotenv()
token = os.getenv('github_token')

api = GhApi(token=token)

r = wonderwords.RandomWord()
noun = r.word(include_parts_of_speech=['noun'])
adjective = r.word(include_parts_of_speech=['adjective'])
name = adjective + '-' + noun

api.repos.create_in_org(org='moco-learn-git', name=name)

print('The GitHub repository you will be working in is moco-learn-git/' + name)
