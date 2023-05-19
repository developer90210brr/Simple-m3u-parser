# M3U Parser

The `M3UParser` class allows parsing M3U files and extracting relevant information such as TVG ID, TVG Name, TVG Logo, Group Title, and URL for each entry. It utilizes the `requests` library for making HTTP requests and the `re` module for regular expression pattern matching.

## Usage

1. Import the required libraries:

    ```python
    import requests
    import re
    ```

2. Instantiate an `M3UParser` object with the URL of the M3U file to parse:

    ```python
    url = "https://example.com/playlist.m3u"
    parser = M3UParser(url)
    ```

3. Parse the M3U file and extract the information:

    ```python
    parser.parse()
    ```

4. Retrieve the parsed entries:

    ```python
    entries = parser.get_entries()
    ```

   The `entries` variable will contain a list of dictionaries, where each dictionary represents an entry in the M3U file. Each entry dictionary includes the following keys:

   - `tvg_id`: The TVG ID of the entry.
   - `tvg_name`: The TVG Name of the entry.
   - `tvg_logo`: The TVG Logo URL of the entry.
   - `group_title`: The Group Title of the entry.
   - `url`: The URL of the entry.

## Example

```python
url = "https://example.com/playlist.m3u"
parser = M3UParser(url)
parser.parse()
entries = parser.get_entries()

for entry in entries:
    print(entry['tvg_name'], entry['url'])