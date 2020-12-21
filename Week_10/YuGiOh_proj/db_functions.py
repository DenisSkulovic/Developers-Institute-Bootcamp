from ygoprodeck import YGOPro
from mainpage.models import Type, Race, Archetype, Cardset, Image, CardPrice, Attribute, Card
from django.core.exceptions import ObjectDoesNotExist
from tqdm import tqdm

def get_api_data():
    ygo = YGOPro()
    data = ygo.get_cards()['data']
    return data


def get_or_create(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except ObjectDoesNotExist:
        return model.objects.create(**kwargs)


def update_db(data):
    for card in tqdm(data):
        entry = {}
        if 'id' in card.keys():
            entry['api_id'] = card['id']
        if 'name' in card.keys():
            entry['name'] = card['name']
        if 'desc' in card.keys():
            entry['desc'] = card['desc']
        if 'type' in card.keys():
            entry['type'] = get_or_create(Type, name=card['type'])
        if 'race' in card.keys():
            entry['race'] = get_or_create(Race, name=card['race'])
        if 'archetype' in card.keys():    
            entry['archetype'] = get_or_create(Archetype, name=card['archetype'])
        if 'atk' in card.keys():
            entry['card_atk'] = card['atk']     
        if 'def' in card.keys():
             entry['card_def'] = card['def'] 
        if 'level' in card.keys():
            entry['card_level'] = card['level']
        if 'attribute' in card.keys():
            entry['attribute'] = get_or_create(Attribute, name=card['attribute'])
        if 'card_sets' in card.keys():  
            card_cardset = [get_or_create(Cardset, 
                                        set_name = cardset['set_name'],
                                        set_code = cardset['set_code'],
                                        set_rarity = cardset['set_rarity'],
                                        set_rarity_code = cardset['set_rarity_code'],
                                        set_price = float(cardset['set_price'])) for cardset in card['card_sets']]
        if 'card_images' in card.keys():
            card_images = [get_or_create(Image, 
                                    api_id=image['id'],
                                    image_url = image['image_url'],
                                    image_url_small = image['image_url_small']) for image in card['card_images']]
        if 'card_prices' in card.keys():
            card_prices = [get_or_create(CardPrice, 
                                    cardmarket_price = float(price['cardmarket_price']),
                                    tcgplayer_price = float(price['tcgplayer_price']),
                                    ebay_price = float(price['ebay_price']),
                                    amazon_price = float(price['amazon_price']),
                                    coolstuffinc_price = float(price['coolstuffinc_price'])) for price in card['card_prices']]
        if not Card.objects.filter(api_id=card['id']):
            new_card = Card.objects.create(**entry)
            new_card.cardset_set = card_cardset
            [new_card.image_set.add(image) for image in card_images]
            [new_card.cardprice_set.add(price) for price in card_prices]
