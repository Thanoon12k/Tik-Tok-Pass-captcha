# Tik-Tok-pass-Capatcha

---

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup & Usage](#setup--usage)
- [Output Guide](#output-guide)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Concurrent Processing**: Uses multithreading to perform checks simultaneously.


## Prerequisites

- **Python**: Ensure you have version 3.x installed (v3.11.5 is recommended).
- **ChromeDriver**: Must be installed and appropriately configured.

## Setup & Usage

1. **Clone the Repository**:
    `git clone https://github.com/Thanoon12k/proxies.git`

2. **Directory Navigation**:
    `cd proxies`
3. **install required packages**:
  
    `pip install -r requirements.txt`

4. **Proxy Setup**: List down your proxy IPs 
in     `proxies.txt`, one IP per line.
    - you can get free proxies for testing use
from [free-proxy-list](https://free-proxy-list.net/)


5. **Execute**:
    
    `python proxies.py`

6. Observe the console for real-time results.

## Output Guide

- For successfully verified proxies:
  `[ THREAD_NAME ] proxy ip : PROXY_IP status : STATUS_CODE resp_ip- RESPONSE_IP`

- For problematic proxies:
  `Error in proxy server, [PROXY_IP]`

## Contributing

Your contributions can make a difference! If you're looking to contribute:

1. **Fork** the repository.
2. Implement your changes.
3. **Open a pull request**.

Feedback, issues, and pull requests are always welcome!

## License

Distributed under the MIT License. See `LICENSE` for more information.

