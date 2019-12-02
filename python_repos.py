import requests

# execute api-calls and stored it
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# let api-repos as an variable
response_dict = r.json()

print("Total repositories:",response_dict['total_count'])

# explored about repositories
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# rearsch first repositories
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)
