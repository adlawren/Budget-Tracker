# TODO
# - Address linter output
# - Look into using an ORM with the database
# - Integrate proper logging framework
# - Unit test the database functions

import argparse

# Local imports
from transaction_record_database_manager import TransactionRecordDatabaseManager
from category_config_parser import CategoryConfigParser
from category_filter import CategoryFilter
from pie_chart_renderer import PieChartRenderer

def import_main(db_path, csv_path):
    TransactionRecordDatabaseManager.import_csv(db_path, csv_path)

def display_main(db_path, yaml_path):
    category_list = CategoryConfigParser.parse_config_file(yaml_path)
    transaction_record_list = TransactionRecordDatabaseManager.get_transaction_records(db_path)
    category_dict = CategoryFilter.filter_categories(transaction_record_list, category_list)
    PieChartRenderer.render(category_dict)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Budget Tracker')
    subparsers = parser.add_subparsers(dest='subparser_name')
    import_parser = subparsers.add_parser(
        'import', description='Import a CSV into a database')
    import_parser.add_argument(
        '--db', help='Path to SQLite database', required=True)
    import_parser.add_argument(
        '--csv', help='Path to CSV', required=True)
    display_parser = subparsers.add_parser(
        'display', description='Display the records from a database')
    display_parser.add_argument(
        '--db', help='Path to SQLite database', required=True)
    display_parser.add_argument(
        '--cfg', help='Path to YAML config', required=True)
    args = parser.parse_args()
    if args.subparser_name == 'import':
        import_main(args.db, args.csv)
    if args.subparser_name == 'display':
        display_main(args.db, args.cfg)
