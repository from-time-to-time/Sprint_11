import pytest
@pytest.mark.xfail(reason="BUG: 'Отменить' не закрывает окно заказа")
def test_order_cancel_closes_order_modal(taxi_order_page):
    # полный флоу до завершённого заказа
    taxi_order_page.select_tariff("Рабочий")
    taxi_order_page.enable_laptop_table()
    search_modal = taxi_order_page.click_submit().wait_visible()
    order_modal = search_modal.wait_until_order_completed().wait_visible()

    order_modal.click_cancel()
    assert order_modal.is_closed()