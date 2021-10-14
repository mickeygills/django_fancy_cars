from django.core.management.base import BaseCommand, CommandError
import requests
from restaurants.models import Restaurant

class Command(BaseCommand):
    def handle(self, *args, **options):
        import requests
        params = {'location':'New York'}

        url = "https://api.yelp.com/v3/businesses/search"

        headers = {"Authorization": "Bearer GxeIBaZxtT3wsibc2t6rHBy0-c2T1yLUx5RCJunRFmZT0tOb6QSFS19iOkMnUfeE66_5Z_kgxIexmTe_ERlEJOFnC0MTzrAvdqd2Lpdivznxju7EJvPR92GmJBdmYXYx"}

        r = requests.get(url, params=params, headers = headers)
        print(r)

        data = requests.get(url, params=params, headers=headers)
        data = data.json()

        # dict_keys(['id', 'alias', 'name', 'image_url', 'is_closed', 'url', 'review_count', 'categories', 'rating', 'coordinates', 'transactions', 'price', 'location', 'phone', 'display_phone', 'distance'])

        for i in data['businesses']:
            try: 
                #print(i)
                #print(i.keys())
                #print('name--->',i['name'])
                #print('image--->',i['image_url'])
                #print('rating--->',i['rating'])
                #print('price--->',i['price'])
                #print('phone--->',i['phone'])
                #print('loc--->',i['location'])
                #print('street_address', i['location']['address1'])
                #print('city', i['location']['city'])
                #print('zip_code', i['location']['zip_code'])
                #print('state', i['location']['state'])
                #print('--------------------------------------')
                value_name = i['name'],
                value_image = i['image_url'],
                value_rating = i['rating'],
                value_price = i['price'],
                value_phone = i['phone'],
                value_address = i['location']['address1'],
                value_city = i['location']['city'],
                value_zip_code = i['location']['zip_code'],
                value_state = i['location']['state'],
                

            except:
                #print('Did not work', i)
                pass

            res, created = Restaurant.objects.get_or_create(
                name = value_name[0],
                phone = value_phone[0],
                address = value_address[0],
                city = value_city[0],
                state = value_state[0],
                zip_code = int(value_zip_code[0]),
                photo = value_image[0],
                price = value_price[0],
                rating = float(value_rating[0]),
                latitude = 0.0,
                longitude = 0.0
            )
            print(res, created)