from enum import Enum


class OrderEnum(Enum):
    PLACED = "placed"
    PREPARING = "preparing"
    BAKING = "baking"
    READY_FOR_DELIVERY = "ready_for_delivery"
    OUT_FOR_DELIVERY = "out_for_delivery"
    DELIVERED = "delivered"
