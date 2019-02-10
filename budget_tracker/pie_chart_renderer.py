import matplotlib.pyplot as plt

class PieChartRenderer:
    @staticmethod
    def render(category_dict):
        labels, colors, amounts = PieChartRenderer.get_chart_arrays(category_dict)
        plt.pie(amounts, labels=labels, colors=colors)
        plt.show()
    @staticmethod
    def get_chart_arrays(category_dict):
        colors = []
        labels = []
        amounts = []
        for category_name in category_dict.keys():
            labels.append(
                f"{category_name}: {category_dict[category_name]['amount']}")
            colors.append(category_dict[category_name]['color'])
            amounts.append(category_dict[category_name]['amount'])
        abs_amounts = []
        for amount in amounts:
            abs_amounts.append(abs(amount))
        return labels, colors, abs_amounts
