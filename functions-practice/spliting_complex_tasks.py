# monthly report for cafe sales, break it down logic wise.
# call generate_report that calls fetch_sales, filter_valid_data, summarize_data!

def fetch_sales():
    print(f'Fetching all the sales data!')


def filter_valid_data():
    print(f'Filtering the valid data!')


def summarize_data():
    print(f'Summarizing the sales data!')

def generate_report():
    fetch_sales()
    filter_valid_data()
    summarize_data()
    print(f'Report is ready!')

generate_report()