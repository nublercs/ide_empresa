from typing import Callable, Optional
from homeassistant.const import UnitOfEnergy
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.typing import (
    ConfigType,
    DiscoveryInfoType,
    HomeAssistantType,
    StateType,
)


def setup_platform(
    hass: HomeAssistantType,
    config: ConfigType,
    async_add_entities: Callable,
    discovery_info: Optional[DiscoveryInfoType] = None,
) -> None:
    sensors = [ConsumoSensor]
    async_add_entities(sensors, update_before_add=True)


class ConsumoSensor(Entity):
    @property
    def name(self) -> str | None:
        return "consumoooxcvds"

    @property
    def state(self) -> StateType:
        return 0

    @property
    def unit_of_measurement(self) -> str | None:
        return UnitOfEnergy.KILO_WATT_HOUR
