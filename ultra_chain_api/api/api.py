from enum import Enum
from typing import Any, Optional
import requests

from ..interfaces.abi_response import AbiResponse
from ..interfaces.account_response import AccountResponse
from ..interfaces.block_reponse import BlockResponse
from ..interfaces.chain_info_response import ChainInfoResponse
from ..interfaces.table_scope import BaseTableResponse, TableResponse
from ..interfaces.transaction_response import TransactionResponse


class UltraAPIError(Exception):
    pass


class TestProducerEndpoint(Enum):
    SEOUL = "https://ultratest-api.eoseoul.io"
    NATION = "http://ultratest.api.eosnation.io"
    RIO = "https://testnet.ultra.eosrio.io"
    USA = "https://test.ultra.eosusa.io"
    LIONS = "https://api.ultra-testnet.cryptolions.io"
    SWEDEN = "https://api.testnet.ultra.eossweden.org"


class MainProducerEndpoint(Enum):
    SEOUL = "https://ultra-api.eoseoul.io"
    NATION = "http://ultra.api.eosnation.io"
    RIO = "https://ultra.eosrio.io"
    USA = "https://ultra.eosusa.io"
    LIONS = "https://api.ultra.cryptolions.io"
    SWEDEN = "https://api.ultra.eossweden.org"


class UltraAPI:
    def __init__(self, producer_endpoint: str):
        self.base_url_v1 = f"{producer_endpoint}/v1"
        self.base_url_v2 = f"{producer_endpoint}/v2"

    def _get(self, endpoint: str, v2: Optional[bool] = False) -> Any:
        """
        Make a GET request to the specified endpoint.
        :param endpoint: The API endpoint to call.
        :return: The response from the API.
        """
        base_url = self.base_url_v2 if v2 else self.base_url_v1
        url = f"{base_url}{endpoint}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def _post(self, endpoint: str, data: dict[str, Any], v2: Optional[bool] = False) -> Any:
        """
        Make a POST request to the specified endpoint.
        :param endpoint: The API endpoint to call.
        :param data: The data to send in the POST request.
        :return: The response from the API.
        """
        base_url = self.base_url_v2 if v2 else self.base_url_v1
        url = f"{base_url}{endpoint}"
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()

    def get_chain_info(self) -> ChainInfoResponse:
        """
        API Docs: https://developers.ultra.io/products/chain-api/get-info.html
        """
        try:
            response = self._get("/chain/get_info")
        except requests.RequestException as e:
            raise UltraAPIError(f"Error fetching chain info: {e}")

        try:
            return ChainInfoResponse(**response)
        except Exception as e:
            raise UltraAPIError(f"Error parsing chain info response: {e}")

    def get_abi(self, account_name: str) -> AbiResponse:
        """
        API Docs: https://developers.ultra.io/products/chain-api/get-abi.html
        """
        try:
            response = self._post("/chain/get_abi", {"account_name": account_name})
        except requests.RequestException as e:
            raise UltraAPIError(f"Error fetching ABI for {account_name}: {e}")

        try:
            return AbiResponse(**response)
        except Exception:
            raise UltraAPIError(f"ABI not found for account {account_name}")

    def get_account(self, account_name: str) -> AccountResponse:
        """
        API Docs: https://developers.ultra.io/products/chain-api/get-account.html
        """
        try:
            response = self._post("/chain/get_account", {"account_name": account_name})
        except requests.RequestException as e:
            raise UltraAPIError(f"Error fetching account {account_name}: {e}")

        try:
            return AccountResponse(**response)
        except KeyError:
            raise UltraAPIError(f"Account not found: {account_name}")

    def get_block(self, block_num_or_id: str) -> BlockResponse:
        """
        API Docs: https://developers.ultra.io/products/chain-api/get-block.html
        """
        try:
            response = self._post("/chain/get_block", {"block_num_or_id": block_num_or_id})
        except requests.RequestException as e:
            raise UltraAPIError(f"Error fetching block {block_num_or_id}: {e}")

        try:
            return BlockResponse(**response)
        except KeyError:
            raise UltraAPIError(f"Block not found: {block_num_or_id}")

    def get_currency_balance(self, code: str, account: str, symbol: str) -> list[str]:
        """
        API Docs: https://developers.ultra.io/products/chain-api/get-currency-balance.html
        """
        try:
            response = self._post("/chain/get_currency_balance", {"code": code, "account": account, "symbol": symbol})
        except requests.RequestException as e:
            raise UltraAPIError(f"Error fetching block currency balance for symbol {symbol}: {e}")

        return response

    def get_table_by_scope(self, code: str, limit: int) -> BaseTableResponse:
        """
        API Docs: https://developers.ultra.io/products/chain-api/get-table-by-scope.html
        """
        try:
            response = self._post("/chain/get_table_by_scope", {"code": code, "limit": limit})
        except requests.RequestException as e:
            raise UltraAPIError(f"Error fetching table by scope: {e}")

        return response

    def get_table_rows(
        self,
        code: str,
        scope: str,
        table: str,
        limit: int,
        lower_bound: Optional[int] = None,
        upper_bound: Optional[int] = None,
    ) -> TableResponse:
        """
        API Docs: https://developers.ultra.io/products/chain-api/get-table-rows.html
        """
        try:
            data = {
                "code": code,
                "scope": scope,
                "table": table,
                "limit": limit,
            }
            if lower_bound is not None:
                data["lower_bound"] = lower_bound
            if upper_bound is not None:
                data["upper_bound"] = upper_bound

            response = self._post("/chain/get_table_rows", data)
        except requests.RequestException as e:
            raise UltraAPIError(f"Error fetching table rows: {e}")

        try:
            return TableResponse(**response)
        except KeyError:
            raise UltraAPIError(f"Table not found: {table}")

    def get_transaction(self, id: str) -> TransactionResponse:
        """
        API Docs: https://developers.ultra.io/products/chain-api/get-transaction.html
        """
        try:
            response = self._get(
                f"/history/get_transaction?id={id}",
                v2=True,
            )
        except requests.RequestException as e:
            raise UltraAPIError(f"Error fetching transaction: {e}")

        try:
            return TransactionResponse(**response)
        except KeyError:
            raise UltraAPIError(f"Transaction not found: {id}")
