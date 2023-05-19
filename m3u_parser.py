import requests
import re

class M3UParser:
    def __init__(self, url):
        """
        Initializes an instance of M3UParser.

        Parameters:
        - url (str): The URL of the M3U file to parse.
        """
        self.url = url
        self.entries = []

    def parse(self):
        """
        Parses the M3U file and extracts relevant information.

        This method retrieves the M3U file from the provided URL, extracts the necessary information such as TVG ID, TVG Name, TVG Logo, Group Title, and URL for each entry, and stores them in the 'entries' list.
        """
        response = requests.get(self.url)
        if response.status_code != 200:
            print("Error: Failed to retrieve the M3U file")
            return

        lines = response.text.split("\n")
        self.entries = []

        for line in lines:
            line = line.strip()
            if line.startswith("#EXTINF:-1"):
                info = line.replace("#EXTINF:-1 ", "")
                
                # Use regex pattern to extract TVG ID, TVG Name, and Group Title
                pattern = r'tvg-id="(.*?)" tvg-name="(.*?)" tvg-logo="(.*?)" group-title="(.*?)"'
                match = re.search(pattern, info)
                
                if match:
                    tvg_id = match.group(1)
                    tvg_name = match.group(2)
                    tvg_logo = match.group(3)
                    group_title = match.group(4)
                    
                    entry = {
                        "tvg_id": tvg_id,
                        "tvg_name": tvg_name,
                        "tvg_logo": tvg_logo,
                        "group_title": group_title,
                        "url": ""
                    }
                    self.entries.append(entry)
            elif line and not line.startswith("#"):
                if self.entries:
                    self.entries[-1]["url"] = line

    def get_entries(self):
        """
        Returns the parsed entries.

        Returns:
        - entries (list): A list of dictionaries containing the parsed entries. Each entry dictionary includes the following keys: 'tvg_id', 'tvg_name', 'tvg_logo', 'group_title', and 'url'.
        """
        return self.entries