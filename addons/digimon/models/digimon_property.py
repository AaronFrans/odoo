from odoo import models, fields, api
import requests
import logging
import base64

_logger = logging.getLogger(__name__)
class DigimonProperty(models.Model):
    _name = "digimon.property"
    _description = "The defining properties of a digimon"
    
    
    name = fields.Char(string="Name", required=True)
    image_url =  fields.Char(string="Image URL", required=True)
    level =  fields.Char(string="Level", required=True)
    
    image = fields.Binary(string="Image", attachment=False,)
    
    @api.model
    def init(self):
        #uncomment for testing
        #self.env['digimon.property'].sudo().search([]).unlink()
        if not self.env['digimon.property'].sudo().search_count([]):
            self.fetch_digimon_data()
    
    
    #data loading via: https://www.youtube.com/watch?v=A0FAIZG90jU
    @api.model
    def fetch_digimon_data(self):
        
        api_url = "https://digimon-api.vercel.app/api/digimon"

        payload = {}
        headers = {}

        response = requests.request("GET", api_url, headers=headers, data=payload)
        
        if response.status_code == 200:
            #make async to speed up load times
            data = response.json()
            for digimon in data:
                digimon_name = digimon['name']
                image_url = digimon['img']
                image_result = self.fetch_image_from_url(digimon['img'])
                
                _logger.info("loading image for %s" % digimon_name)
                self.env['digimon.property'].sudo().create({
                    'name': digimon_name,
                    'image_url': image_url,
                    'level': digimon['level'],
                    'image': image_result
                })

    #code via: https://holdenrehg.com/blog/2019-02-04_odoo-images-and-attachments-load-from-url
    def fetch_image_from_url(self, url):
        """
        Gets an image from a URL and converts it to an Odoo friendly format
        so that we can store it in a Binary field.
        :param url: The URL to fetch.
        :return: Returns a base64 encoded string.
        """
        
        data = ""
        
        try:
            # Python 2
            # data = requests.get(url.strip()).content.encode("base64").replace("\n", "")
            # Python 3
            data = base64.b64encode(requests.get(url.strip()).content).replace(b"\n", b"")
            
        except Exception as e:
            _logger.warning("There was a problem requesting the image from URL %s" % url)
            logging.exception(e)
        return data