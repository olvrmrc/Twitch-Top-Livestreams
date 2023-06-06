# Twitch Top Livestreams

> *"Twitch Top Livestreams"* is a Python project that allows you to fetch the usernames of the streamers who are currently broadcasting (the most popular) livestreams on [twitch.tv](https://twitch.tv/) by utilizing the Twitch Helix API.

## Table of Contents
- [Installation](#Installation)
- [Usage](#Usage)
- [Features](#Features)
- [Contributing](#Contributing)
- [License](#License)

## Installation

Clone this repository to your local machine:
```sh
git clone https://github.com/olvrmrc/Twitch-Top-Livestreams.git
```

Navigate to the projects directory:
```sh
cd Twitch-Top-Livestreams
```

Install the dotenv library using pip:
```sh
pip install python-dotenv
```

## Usage

Obtain a Twitch API client ID and client secret by [creating a Twitch developer account](https://dev.twitch.tv/) and [registering a new application](https://dev.twitch.tv/console/apps/create):
Create new application             |  Copy your applications ID and secret
:-------------------------:|:-------------------------:
![](https://github.com/olvrmrc/colours/assets/89043452/014a54a1-4b32-40d8-bbc2-f09feb73adb6)  |  ![](https://github.com/olvrmrc/colours/assets/89043452/9c89a191-3e3a-44c0-9881-8952e11672b7)

Create an .env file in the projects root folder and save both the client ID and the client secret as shown below:
![image](https://github.com/olvrmrc/colours/assets/89043452/8f5c6540-2f41-4431-aa57-7b9c035d415f)

Obtain an OAuth 2.0 Token by running *api_token.py* and save it to your .env file:
![image](https://github.com/olvrmrc/colours/assets/89043452/d5b51b38-fa31-479f-bf0c-d5f731c993d2)

Modify the variables in lines 11 to 15 *main.py* as you need them:
| Name | Value | Explanation |
| ------ | ------ | ------ |
| MIN | Minimum number of viewers | Only streams whose number of viewers is equal or greater will be saved |
| MAX | Maximum number of viewers | Only streams whose number of viewers is equal or less will be saved |
| PAGES | Number of pages that will be loaded | A page contains 100 streams, the pages are sorted by number of viewers |
| LANGUAGES | List of specific languages | You may specify one or multiple ISO 639-1 two-letter language codes |
| GAMES | List of specific games which will be checked | Simply delete or comment out any games you don't need |

Run the *main.py* file. A list of the streams will be saved to *output.txt*.

## Features

1. Obtains a list of the most-watched livestreams on twitch.tv.
2. Has the ability to sort after specific numbers of viewers, languages and games.
3. Saves the usernames of the streamers to a text file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

>Copyright © 2023 Marc Szigethy
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.