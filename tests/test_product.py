from app.views import product

def test_product(client):
    product_page = client.get("/product/99999")
    assert product_page.status_code == 200
    
    # Some basic checks to make sure it is showing the right data
    assert b'TestProduct' in product_page.data
    assert b'Add to Basket' in product_page.data
    assert b'This is a test description' in product_page.data