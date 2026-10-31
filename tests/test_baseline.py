from order_status.analytics_observer import AnalyticsObserver
from order_status.audit_observer import AuditObserver
from order_status.customer_notifier import CustomerNotifier
from order_status.order_status import OrderStatus


def test_observers_receive_updates_until_unsubscribed():
    customer = CustomerNotifier()
    audit = AuditObserver()
    analytics = AnalyticsObserver()
    order = OrderStatus("A-100")

    order.subscribe(customer)
    order.subscribe(audit)
    order.subscribe(analytics)
    order.set_status("SHIPPED")

    assert order.status == "SHIPPED"
    assert customer.messages == ["A-100:SHIPPED"]
    assert audit.entries == [("A-100", "SHIPPED")]
    assert analytics.events == [{"order_id": "A-100", "status": "SHIPPED"}]

    order.unsubscribe(analytics)
    order.set_status("DELIVERED")

    assert order.status == "DELIVERED"
    assert customer.messages == ["A-100:SHIPPED", "A-100:DELIVERED"]
    assert audit.entries == [("A-100", "SHIPPED"), ("A-100", "DELIVERED")]
    assert analytics.events == [{"order_id": "A-100", "status": "SHIPPED"}]
