import requests

bot_token = '6462919475:AAH6Y9JFKomqiIjKBa4kZNcSD7FnvHBHuFs'
webhook_url = ('https://ubdbeton.com/bot/webhook/')

telegram_api_url = f'https://api.telegram.org/bot{bot_token}/setWebhook?url={webhook_url}'
response = requests.get(telegram_api_url)
print(response.json())

