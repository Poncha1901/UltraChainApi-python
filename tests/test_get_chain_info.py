from ultra_chain_api.interfaces.chain_info_response import ChainInfoResponse


def test_get_chain_info() -> None:
    """
    Test the get_chain_info method of the UltraAPI class.
    """
    from ultra_chain_api import TestProducerEndpoint, UltraAPI

    client = UltraAPI(producer_endpoint=TestProducerEndpoint.SWEDEN.value)
    chain_info = client.get_chain_info()

    assert isinstance(chain_info, ChainInfoResponse), "Expected ChainInfoResponse type"
