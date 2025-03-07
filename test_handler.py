import handler

def test_scrape_mitula():
    event = {}
    context = {}
    resultado = handler.scrape_mitula(event, context)
    assert resultado == {"status": "OK"}

