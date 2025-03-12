import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to extract relevant information from a Soccerway page
def extract_from_soccerway(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract team name (for example, from a specific tag, modify as per website structure)
        team_name = soup.find('h1', {'class': 'team-name'}).text.strip() if soup.find('h1', {'class': 'team-name'}) else 'TBC'

        # Extract stadium name
        stadium_name = soup.find('div', {'class': 'stadium-name'}).text.strip() if soup.find('div', {'class': 'stadium-name'}) else 'TBC'

        # Extract city
        city = soup.find('span', {'class': 'city'}).text.strip() if soup.find('span', {'class': 'city'}) else 'TBC'

        # You can similarly extract other fields as needed by inspecting the HTML structure
        country = 'TBC'  # Placeholder until more info is extracted
        transfermarkt_link = 'TBC'  # Placeholder
        
        return {
            'Team Name': team_name,
            'Stadium Name': stadium_name,
            'City': city,
            'Country': country,
            'Soccerway': url,
            'Transfermarkt': transfermarkt_link,
            'Division': 'TBC',  # Example data, adjust based on HTML parsing
            # Add other fields as per sample structure
        }
    except Exception as e:
        print(f"Error extracting from {url}: {e}")
        return None

# Function to process each URL
def process_links(links):
    data = []
    for link in links:
        if 'soccerway.com' in link:
            data.append(extract_from_soccerway(link))
        # Add other websites as needed, e.g., Transfermarkt.com
        # elif 'transfermarkt.com' in link:
        #     data.append(extract_from_transfermarkt(link))
    
    return data

# Load input file with URLs
input_file_path = 'C:\\Users\\aswin\\Programming\\input_links.xlsx'
input_df = pd.read_excel(input_file_path)
links = input_df.iloc[:, 0].tolist()  # Assuming the URLs are in the first column

# Process each URL and gather data
data = process_links(links)

# Create a DataFrame for output
output_df = pd.DataFrame(data)

# Match the structure of Sample.xlsx
columns = [
    'Row Number', 'Team Name', 'Soccerway', 'Transfermarkt', 'Flashscore', 'City', 
    'Stadium Name', 'Country', 'Address of Stadium', 'Division', 'Google News Link',
    'TotalCorner', 'BMBets', 'Elevation (m)', 'Weather', 'TBC', 'TBC.1', 'TBC.2'
    # Add other columns as needed
]
output_df = output_df.reindex(columns=columns)

# Save to an Excel file
output_file_path = 'C:\\Users\\aswin\\Programming\\output_file.xlsx'
output_df.to_excel(output_file_path, index=False)

print(f"Data extraction complete. Output saved to {output_file_path}")
