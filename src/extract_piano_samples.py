from bs4 import BeautifulSoup

def extract_hrefs(input_path, output_path):
    # Read the HTML content from the input file
    with open(input_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'lxml')

    # Open the output file in write mode
    with open(output_path, 'w', encoding='utf-8') as file:
        # Find all <a> tags in the HTML content
        for a_tag in soup.find_all('a', href=True):
            # Extract the href attribute
            href = a_tag['href']
            # Write the href to the output file
            file.write(href + '\n')

if __name__ == "__main__":
    # Define input and output paths
    input_path = 'C:/atari-monk/code/piano/data/piano_samples/links.html'  # Replace with your input file path
    output_path = 'C:/atari-monk/code/piano/data/piano_samples/all_notes.txt'    # Replace with your desired output file path

    # Call the function
    extract_hrefs(input_path, output_path)
