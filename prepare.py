import os, json

phone = os.environ.get('CMCC_PHONE', '13663992899')
token = os.environ.get('CMCC_APP_TOKEN', '')
tpl_str = os.environ.get('CMCC_SESSION_TEMPLATE', '{}')

# 1. 写 config.json
with open('config.json', 'w') as f:
    json.dump({'phone': phone, 'app_token': token}, f)
    
# 2. 写 session 文件（解决 KeyError）
try:
    tpl = json.loads(tpl_str)
except:
    tpl = {}
    
profile = {
    'url': 'https://client.app.coc.10086.cn/biz-orange/LN/uamonekeylogin/autoLogin',
    'cookie': '',
    'template': tpl,
    'xk': tpl.get('xk', ''),
    'phone': phone
}
with open(f'.cmcc_session_{phone[-4:]}.json', 'w') as f:
    json.dump(profile, f)
