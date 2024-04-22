from transifex.native import init
from transifex.native import tx
from transifex.native.parsing import SourceString

# Inialize SDK
#init(token="PUBLIC-TOKEN", secret="SECRET", languages=[])
init('1/5e2c211e9b3833e57188466500c73260e5c24cee', ['fr', 'de', 'pt', 'es_MX'], '1/9d8bbe8e701521fb3fdcca11a15cee4aa687735e')

# Add some strings to push
strings = [
    SourceString("Welcome to Transifex"),
    SourceString("This is a python test")]

# Check response code
response_code, response_content = tx.push_source_strings(strings)
print(response_content)

# Poll job for results
job_url = response_content['data']['links']['job']
status = 'starting'
while status in ['starting', 'pending', 'processing']:
    status_code, response_content = tx.get_push_status(job_url)
    print(response_content)

    status = response_content['data']['status']

    

print('Done')
