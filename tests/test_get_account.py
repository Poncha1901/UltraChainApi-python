from ultra_chain_api.interfaces.account_response import AccountResponse


def test_get_account() -> None:
    """
    Test the get_account method of the UltraAPI class.
    """
    from ultra_chain_api import TestProducerEndpoint, UltraAPI

    client = UltraAPI(producer_endpoint=TestProducerEndpoint.SWEDEN.value)
    account_response = client.get_account("ultra")

    assert isinstance(account_response, AccountResponse), "Expected AccountResponse type"
    assert account_response.account_name == "ultra", "Account name mismatch"
