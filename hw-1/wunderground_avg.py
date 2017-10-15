import sys

REPORT_STRING = '''Summary of daily temperature data for {} in year 2016'''
DATASOURCE_FOLDER = 'data_source'
USAGE_STRING = '''Error: {}
Usage:
      wunderground_avg.py computes the 2016 avg temp,
      max temp, min temp and
      standard deviation for a given city.
Valid cities are: New York, Chicago, Honolulu, Los Angeles.'''

def info_logging(msg):
    '''log message to the terminal'''
    exit(USAGE_STRING.format(msg))

def validate_input(arg):
    '''validates and normalize the command line argument'''
    if not len(sys.argv) == 2:
        info_logging('please enter the required argument')
    return "".join(arg[1].lower().split())

def format_dataset(location):
    '''extracts data from csv into a 2D list'''
    try:
        with open('{}/weather_{}.csv'.format(DATASOURCE_FOLDER, location)) as f:
            fh = f.read().strip()
    except IOError:
        info_logging("Argument could not be matched to any dataset")
    data = [row.split(',') for row in fh.split('\n')]
    del data[0]
    return data

def calculate_temp(data):
    '''calculates min, max, mean and standart deviation from data'''
    temp = [int(i[2]) for i in data]
    mean_temp, max_temp, min_temp = sum(temp) / len(temp), max(temp), min(temp)
    sd = (sum([(int(i) - mean_temp)**2 for i in temp]) / float(len(temp)))**(0.5)
    return {'average_temp': mean_temp, 'min_temp': min_temp, 'max_temp': max_temp, 'standard_deviation': sd}

def report_temps(temp_data):
    '''formats and outputs result'''
    report_data = [REPORT_STRING.format(sys.argv[1])]
    for item in temp_data:
        report_data.append("{}: {}".format(item.replace("_", " "), temp_data[item]))
    print("\n".join(report_data))

def main():
    '''main program entry point'''
    city = validate_input(sys.argv)
    data = format_dataset(city)
    temp_data = calculate_temp(data)
    report_temps(temp_data)

if __name__ == '__main__':
    main()
