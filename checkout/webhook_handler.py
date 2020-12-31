from django.http import HttpResponse


class StripeWH_handler:
    """Handle stripe webhook"""

    def __init__(self, request):
        self.request = request

    def handler_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status:200)