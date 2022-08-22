import html
import client 
import json
import time

class TempMail:
    def __init__(self, proxies: str = None, timeout: int = 15, bearer_token: str or None = None) -> None:
        self.session = client.init()
        self.base_url = 'https://web2.temp-mail.org'
        self.proxies = proxies
        self.timeout = timeout
        
        self.session.headers['authorization'] = f'Bearer {bearer_token}' if bearer_token else None

    def get_mail(self) -> str:
        status: html = self.session.get(
            url     = f'{self.base_url}', 
            proxies = self.proxies, 
            timeout = self.timeout
        ).status_code
        try:
            if status == 200:
                data = self.session.post(
                    url     = f'{self.base_url}/mailbox', 
                    proxies = self.proxies, 
                    timeout = self.timeout
                ).json()
                self.session.headers['authorization'] = f'Bearer {data["token"]}'
                return data["token"], data["mailbox"]
        except:
            return 'Email creation error.'
    
    def fetch_inbox(self) -> json:
        response = self.session.get(
            url = f'{self.base_url}/messages',
                proxies = self.proxies, 
                timeout = self.timeout
        ).json()
        return response
    
    def get_message_content(self, message_id: str):
        response = self.session.get(
            url = f'{self.base_url}/messages/{message_id}',
            proxies = self.proxies, 
            timeout = self.timeout
        ).json()
        return response["bodyHtml"]
