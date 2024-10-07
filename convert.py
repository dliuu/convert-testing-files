import re
import csv

# Change filenames and input path
input_file = "raw_data/fields.json"
output_file = "output.csv"


def extract_labels_and_values(js_data):
    '''
    Extracts only the label and DefaultValue fields from Bernard's json files
    '''
    # python regex is dumb, ask chatgpt to explain and write
    labels = re.findall(r'label:\s*"([^"]+)"', js_data)
    default_values = re.findall(r'defaultValue:\s*"([^"]*)"', js_data)
    
    #handling nulls
    while len(default_values) < len(labels):
        default_values.append('')

    return labels, default_values


def write_to_csv(labels, default_values, output_file):
    '''
    Writes data to a new csv file. 
    Modify the output name at top of script
    '''
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(labels)
        writer.writerow(default_values)


def main():
    try:
        with open(input_file, 'r') as f:
            js_data = f.read()

        labels, default_values = extract_labels_and_values(js_data)
        write_to_csv(labels, default_values, output_file)

        print(f"Data has been written to {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
