from src.domain.entitys.cart_item import CartItemModel

class CartItemPriceCalculator:
    @staticmethod
    def calculate_total_price(cart_item: CartItemModel) -> float:
        return sum(entry.item.price * entry.quantity for entry in cart_item.items)
