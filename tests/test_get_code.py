from ultra_chain_api.interfaces.code_response import CodeResponse


def test_get_code() -> None:
    """
    Test the get_code method of the UltraAPI class.
    """
    from ultra_chain_api import TestProducerEndpoint, UltraAPI

    client = UltraAPI(producer_endpoint=TestProducerEndpoint.SWEDEN.value)
    code_response = client.get_code("ultra.tools")

    assert isinstance(code_response, CodeResponse), "Expected str type"
