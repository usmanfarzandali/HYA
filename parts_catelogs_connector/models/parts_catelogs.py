# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
import requests


class PartsCatelogs(models.Model):
    _name = "parts.catelogs"


    name = fields.Char('Name')
    url_ip = fields.Char('URL for IP')
    url_catelog = fields.Char('URL for Catelog')
    api_key = fields.Char('API')
    result = fields.Text('API Testing Result')

    @api.multi
    def get_catalogs(self):
        for rec in self:
            headers = {"accept":"application/json",
                    "Accept-Language":"en",}
            
            
            headers.update({"Authorization": rec.api_key})
            url = rec.url_catelog
            response = requests.get(url,headers=headers)
            #rec.result = response.content
            rec.result = response.json()


    @api.multi
    def get_ip(self):
        for rec in self:
            headers = {"accept":"application/json"}
            url = rec.url_ip
            response = requests.get(url,headers=headers)
            #rec.result = response.content
            rec.result = response.json()
            


