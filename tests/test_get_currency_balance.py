def test_get_currency_balance() -> None:
    """
    Test the get_currency_balance method of the UltraAPI class.
    """
    from ultra_chain_api import TestProducerEndpoint, UltraAPI

    client = UltraAPI(producer_endpoint=TestProducerEndpoint.SWEDEN.value)
    balance_response = client.get_currency_balance("eosio.token", "ultra.nft.ft", "UOS")

    assert isinstance(balance_response, list), "Expected list type"
    assert len(balance_response) == 1, "Expected length 1"
