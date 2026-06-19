from django.core.management.base import BaseCommand, CommandError
import requests
from yugioh.models import CardDetails, Rarity, CardType, MonsterType, MonsterAttribute, FrameType, Series, PrintSeries

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        all_cards = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php').json()

        for card in all_cards['data']:
            card_type = None
            race = None
            frame_type = None
            attribute = None
            if card.get('type'):
                obj, created = CardType.objects.get_or_create(
                    name = card['type']
                )
                if created:
                    print(card['type'])
                card_type = obj
            if card.get('race'):
                obj, created = MonsterType.objects.get_or_create(
                    name = card['race']
                )
                if created:
                    print(card['race'])
                race = obj
            if card.get('attribute'):
                obj, created = MonsterAttribute.objects.get_or_create(
                    name = card['attribute']
                )
                if created:
                    print(card['attribute'])
                attribute = obj
            if card.get('frameType'):
                obj, created = FrameType.objects.get_or_create(
                    name = card['frameType']
                )
                if created:
                    print(card['frameType'])
                frame_type = obj
            card_img = card.get('card_images')
            obj, created = CardDetails.objects.get_or_create(
                name            = card['name'],
                defaults={
                    'card_type'         : card_type,
                    'monster_type'      : race,
                    'frame_type'        : frame_type,
                    'monster_attribute' : attribute,
                    'description'       : card['desc'],
                    'image'             : card.get('card_images',[])[0]['image_url'] if card_img else None,
                    'level'             : card.get('level'),
                    'attack'            : card.get('atk'),
                    'defense'           : card.get('def'),
                }
            )
            if created:
                print(card['name'])
            full_card = obj
        
            if card.get('card_sets'):

                for series_name in card['card_sets']:
                    obj, created = Series.objects.get_or_create(
                        name = series_name['set_name']
                    )
                    the_series_name = obj
                    obj, created = Rarity.objects.get_or_create(
                        name = series_name['set_rarity']
                    )
                    the_series_rarity = obj
                    obj, created = PrintSeries.objects.get_or_create(
                        card = full_card,
                        full_series = the_series_name,
                        defaults={
                            'rarity'        : the_series_rarity,
                            'series_code'   : series_name['set_code']
                        }
                    )
                