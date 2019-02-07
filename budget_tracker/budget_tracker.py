# TODO
# - Use CLI framework
# - Unit test the database functions
# - Test the run scripts when the db/ directory doesn't exist
# - Look into using an ORM with the database
# - Only process expenses from the last month
# - Add a ./script/backup script - backup database file to.. somewhere

# Local imports
from transaction_record_database_manager import TransactionRecordDatabaseManager
from category_config_parser import CategoryConfigParser
from category_filter import CategoryFilter
from pie_chart_renderer import PieChartRenderer

CSV_PATH = '/home/al/Sync/statement_cleaned.csv'
DB_PATH = '/home/al/Git-Repos/Budget-Tracker/db/transaction_records.db'
YAML_PATH = '/home/al/Git-Repos/Budget-Tracker/categories.yaml'


# TODO:
# - Parse command line options
#   - Import csv
#   - display diagram [default]
if __name__ == '__main__':
    #TransactionRecordDatabaseManager.import_csv(CSV_PATH, DB_PATH)
    category_list = CategoryConfigParser.parse_config_file(YAML_PATH)
    transaction_record_list = TransactionRecordDatabaseManager.get_transaction_records(DB_PATH)
    category_dict = CategoryFilter.filter_categories(transaction_record_list, category_list)
    PieChartRenderer.render(category_dict)
