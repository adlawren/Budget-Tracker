class CategoryFilter:
    @staticmethod
    def filter_categories(transaction_record_list, category_list):
        category_dict = {}
        for transaction_record in transaction_record_list:
            for category in category_list:
                category_found = False
                for matcher in category['matchers']:
                    if matcher.match(transaction_record):
                        category_attributes = category['attributes']
                        if category_attributes.log:
                            print(
                                f'Note: \'{category_attributes.name}\' category matched: {transaction_record.desc}'
                            )
                        if category_attributes.show:
                            if category_attributes.name in category_dict:
                                category_dict[category_attributes.name][
                                    'amount'] += transaction_record.amount
                            else:
                                category_dict[category_attributes.name] = {
                                    'color': category_attributes.color,
                                    'amount': transaction_record.amount
                                }
                        category_found = True
                        break
                if category_found:
                    break
        return category_dict
