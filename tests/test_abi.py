from ultra_chain_api.interfaces.abi_response import AbiResponse


def test_get_abi() -> None:
    from ultra_chain_api import TestProducerEndpoint, UltraAPI

    """
    Test the get_abi method of the UltraAPI class.
    """

    client = UltraAPI(producer_endpoint=TestProducerEndpoint.SWEDEN.value)
    abi_response = client.get_abi("ultra.tools")

    assert isinstance(abi_response, AbiResponse), "Expected AbiResponse type"
    assert abi_response.account_name == "ultra.tools", "Account name mismatch"
