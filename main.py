from pyNutriScore import NutriScore

result = NutriScore().calculate_class(
    {
        'energy': 0,
        'fibers': 4,
        'fruit_percentage': 60,
        'proteins': 2,
        'saturated_fats': 2,
        'sodium': 500,
        'sugar': 10,
    },
    'solid'  # either 'solid' or 'beverage'
)

print(result)  # Output: "B" 

# from pyNutriScore import NutriScore

# result = NutriScore().calculate_class(
#     {
#         'energy': 0,
#         'fibers': 4,
#         'fruit_percentage': 60,
#         'proteins': 2,
#         'saturated_fats': 2,
#         'sodium': 500,
#         'sugar': 10,
#     },
#     'solid'  # either 'solid' or 'beverage'
# )

# print(result)  # Output: "B"