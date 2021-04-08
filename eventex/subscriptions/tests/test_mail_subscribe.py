from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r

class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Valério Farias', cpf='12345678901',
                    email='valeriofc@gmail.com', phone='8488888888')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]
        
    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        
        self.assertEqual(expect, self.email.subject)
        
    def test_subscription_email_from(self):
        expect = 'valeriofc@gmail.com'   
        
        self.assertEqual(expect, self.email.from_email)
    
    def test_subscription_email_to(self):
        expect = ['valeriofc@gmail.com', 'valeriofc@gmail.com']
        
        self.assertEqual(expect, self.email.to)
        
    def test_subscription_email_body(self):
        contents = [
            'Valério Farias',
            '12345678901',
            'valeriofc@gmail.com',
            '8488888888',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

