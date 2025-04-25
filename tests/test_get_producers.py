from ultra_chain_api.interfaces.producer_response import ProducersResponse


def test_get_producers() -> None:
    """
    Test the get_producers method of the UltraAPI class.
    """
    from ultra_chain_api import TestProducerEndpoint, UltraAPI

    client = UltraAPI(producer_endpoint=TestProducerEndpoint.SWEDEN.value)
    producers_response = client.get_producers()

    assert isinstance(producers_response, ProducersResponse), "Expected list type"
    assert len(producers_response.rows) > 0, "Expected non-empty list"
