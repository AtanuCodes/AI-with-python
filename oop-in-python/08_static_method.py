# class ChaiUtils:
#     @staticmethod
#     def make_chai(milk, tea_leaves):
#         return f"Making chai with {milk} and {tea_leaves}"
# print(ChaiUtils.make_chai('whole milk', 'assam tea leaves'))


class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(',')]
ingredients = "  whole milk,  assam tea leaves,  ginger,  cardamom "
print(ChaiUtils.clean_ingredients(ingredients))