# UltraChainApi-python

UltraChainApi-python is a Python library designed to interact with the blockchain API seamlessly. It provides an easy-to-use interface for developers to integrate blockchain functionalities into their Python applications.

## Features

- Simplified access to blockchain API endpoints.
- Lightweight and easy to integrate.
- Designed for Python developers.

## Installation

```bash
pip install ultra-chain-api
```

## Usage

```python
from ultra_chain_api import UltraAPI

# Can also import the producers
# from ultra_chain_api import MainProducerEndpoint
# client = UltraAPI(producer_endpoint=MainProducerEndpoint.SWEDEN.value)


client = UltraAPI(producer_endpoint="producer endpoint url")
response = client.get_info()
print(response)
```

## License

This project is licensed under the MIT License.
