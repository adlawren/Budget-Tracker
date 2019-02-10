class CategoryAttributes:
    def __init__(self, category_name, attribute_dict):
        self.name = category_name
        self.color = attribute_dict['color']
        self.show = attribute_dict['show'] if 'show' in attribute_dict else True
        self.log = attribute_dict['log'] if 'log' in attribute_dict else False
