from ultra_chain_api.interfaces.transaction_response import TransactionResponse


def test_get_transaction() -> None:
    """
    Test the get_transaction method of the UltraAPI class.
    """
    from ultra_chain_api import TestProducerEndpoint, UltraAPI

    client = UltraAPI(producer_endpoint=TestProducerEndpoint.SWEDEN.value)
    transaction_response = client.get_transaction("a0609944c6be737c39e26ad78314f154a017030896a8bc769f5dc00bf9941bde")

    assert isinstance(transaction_response, TransactionResponse), "Expected TransactionResponse type"
    assert transaction_response.trx_id == "a0609944c6be737c39e26ad78314f154a017030896a8bc769f5dc00bf9941bde", (
        "Transaction ID mismatch"
    )
