# Patrón Observer

- **Subject:** `OrderStatus` mantiene el estado del pedido y una lista de observadores. Permite suscribirlos con `subscribe` y retirarlos con `unsubscribe`.
- **Observer:** define el contrato abstracto `update(order_id, status)`.
- **Concrete Observers:** `CustomerNotifier`, `AuditObserver` y `AnalyticsObserver` implementan ese contrato. Cada uno reacciona al cambio de forma independiente.

Al ejecutar `set_status`, primero se actualiza el estado y luego se recorre la lista para llamar a `update` en cada observador. `OrderStatus` solo depende del contrato `Observer`; no importa ni conoce las clases concretas.

## Agregar Analytics sin cambiar la notificación

El código que configura los objetos crea un `AnalyticsObserver` y lo suscribe. No es necesario agregar una llamada especial ni un `if` en `OrderStatus`:

```python
from order_status.analytics_observer import AnalyticsObserver
from order_status.audit_observer import AuditObserver
from order_status.customer_notifier import CustomerNotifier
from order_status.order_status import OrderStatus

order = OrderStatus("A-100")
customer = CustomerNotifier()
audit = AuditObserver()
analytics = AnalyticsObserver()

order.subscribe(customer)
order.subscribe(audit)
order.subscribe(analytics)
order.set_status("SHIPPED")

order.unsubscribe(analytics)
order.set_status("DELIVERED")
```

Los tres reciben `SHIPPED`. Después de retirar Analytics, solo CustomerNotifier y AuditObserver reciben `DELIVERED`.

## Costo de ciclo de vida

Hay que administrar las suscripciones: cuando un observador deja de necesitar avisos, debe desuscribirse. Si se olvida, seguirá recibiendo actualizaciones y `OrderStatus` conservará una referencia a ese objeto, manteniéndolo en memoria mientras lo retenga.

## Prueba enfocada

Se actualizó la prueba original para verificar el cambio de estado, la notificación a los tres observadores y que Analytics deje de recibir eventos después de desuscribirse, mientras los otros dos siguen recibiéndolos.

Ejecutar desde la carpeta del proyecto:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```
