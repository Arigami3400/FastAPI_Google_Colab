from fastapi import APIRouter
from colab_app.db.schema import MashSchema
import joblib



model = joblib.load('colab_app/scaler_model/model_mash.pkl')
scaler = joblib.load('colab_app/scaler_model/scaler_mash.pkl')

mashrooms_router = APIRouter(prefix='/predict_mashrooms', tags=['/predict_mashrooms'])




cap_shape_list = ['c', 'f', 'k', 's', 'x']
cap_surface_list = ['g', 's', 'y']
cap_color_list = ['c', 'e', 'g', 'n', 'p', 'r', 'u', 'w', 'y']
bruises_list = ['t']
odor_list = ['c', 'f', 'l', 'm', 'n', 'p', 's', 'y']
gill_attachment_list= ['f']
gill_spacing_list = ['w']
gill_size_list = ['n']
gill_color_list = ['e', 'g', 'h', 'k', 'n', 'o', 'p', 'r', 'u', 'w', 'y']
stalk_shape_list = ['t']
stalk_root_list = ['c', 'e', 'r']
stalk_surface_above_ring_list = ['k', 's', 'y']
stalk_surface_below_ring_list = ['k', 's', 'y']
stalk_color_above_ring_list = ['c', 'e', 'g', 'n', 'o', 'p', 'w', 'y']
stalk_color_below_ring_list = ['c', 'e', 'g', 'n', 'o', 'p', 'w', 'y']
veil_color_list = ['o', 'w', 'y']
ring_number_list = ['o', 't']
ring_type_list = ['f', 'l', 'n', 'p']
spore_print_color_list = ['h', 'k', 'n', 'o', 'r', 'u', 'w', 'y']
population_list = ['c', 'n', 's', 'v', 'y']
habitat_list = ['g', 'l', 'm', 'p', 'u', 'w']


@mashrooms_router.post('/')
async def predict(mash1: MashSchema):
    mash_dict = mash1.dict()

    cap_shape = mash_dict.pop('cap_shape')
    cap_shape1_0 = [
        1 if cap_shape == i else 0 for i in cap_shape_list
    ]

    cap_surface = mash_dict.pop('cap_surface')
    cap_surface1_0 = [
        1 if cap_surface == i else 0 for i in cap_surface_list
    ]

    cap_color = mash_dict.pop('cap_color')
    cap_color1_0 = [
        1 if cap_color == i else 0 for i in cap_color_list
    ]

    bruises = mash_dict.pop('bruises')
    bruises1_0 = [
        1 if bruises == i else 0 for i in bruises_list
    ]

    odor = mash_dict.pop('odor')
    odor1_0 = [
        1 if odor == i else 0 for i in odor_list
    ]

    gill_attachment = mash_dict.pop('gill_attachment')
    gill_attachment1_0 = [
        1 if gill_attachment == i else 0 for i in gill_attachment_list
    ]

    gill_spacing = mash_dict.pop('gill_spacing')
    gill_spacing1_0 = [
        1 if gill_spacing == i else 0 for i in gill_spacing_list
    ]

    gill_size = mash_dict.pop('gill_size')
    gill_size1_0 = [
        1 if gill_size == i else 0 for i in gill_size_list
    ]

    gill_color = mash_dict.pop('gill_color')
    gill_color1_0 = [
        1 if gill_color == i else 0 for i in gill_color_list
    ]

    stalk_shape = mash_dict.pop('stalk_shape')
    stalk_shape1_0 = [
        1 if stalk_shape == i else 0 for i in stalk_shape_list
    ]

    stalk_root = mash_dict.pop('stalk_root')
    stalk_root1_0 = [
        1 if stalk_root == i else 0 for i in stalk_root_list
    ]

    stalk_surface_above_ring = mash_dict.pop('stalk_surface_above_ring')
    stalk_surface_above_ring1_0 = [
        1 if stalk_surface_above_ring == i else 0 for i in stalk_surface_above_ring_list
    ]

    stalk_surface_below_ring = mash_dict.pop('stalk_surface_below_ring')
    stalk_surface_below_ring1_0 = [
        1 if stalk_surface_below_ring == i else 0 for i in stalk_surface_below_ring_list
    ]

    stalk_color_above_ring = mash_dict.pop('stalk_color_above_ring')
    stalk_color_above_ring1_0 = [
        1 if stalk_color_above_ring == i else 0 for i in stalk_color_above_ring_list
    ]

    stalk_color_below_ring = mash_dict.pop('stalk_color_below_ring')
    stalk_color_below_ring1_0 = [
        1 if stalk_color_below_ring == i else 0 for i in stalk_color_below_ring_list
    ]

    veil_color = mash_dict.pop('veil_color')
    veil_color1_0 = [
        1 if veil_color == i else 0 for i in veil_color_list
    ]

    ring_number = mash_dict.pop('ring_number')
    ring_number1_0 = [
        1 if ring_number == i else 0 for i in ring_number_list
    ]

    ring_type = mash_dict.pop('ring_type')
    ring_type1_0 = [
        1 if ring_type == i else 0 for i in ring_type_list
    ]

    spore_print_color = mash_dict.pop('spore_print_color')
    spore_print_color1_0 = [
        1 if spore_print_color == i else 0 for i in spore_print_color_list
    ]

    population = mash_dict.pop('population')
    population1_0 = [
        1 if population == i else 0 for i in population_list
    ]

    habitat = mash_dict.pop('habitat')
    habitat1_0 = [
        1 if habitat == i else 0 for i in habitat_list
    ]
    features =  ( cap_shape1_0 + cap_surface1_0 + cap_color1_0 + bruises1_0 + odor1_0 + gill_attachment1_0 +
                gill_spacing1_0 + gill_size1_0 + gill_color1_0 + stalk_shape1_0 + stalk_root1_0 +
                stalk_surface_above_ring1_0 + stalk_surface_below_ring1_0 + stalk_color_above_ring1_0
                + stalk_color_below_ring1_0 + veil_color1_0 + ring_number1_0 + ring_type1_0 + spore_print_color1_0 + population1_0 + habitat1_0 )
    scaled_data = scaler.transform([features])
    pred = model.predict(scaled_data)[0]
    if pred == 1:
        pred = 'edible'
    else:
        pred = 'poisonous'

    return{'predict': pred}