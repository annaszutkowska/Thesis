from .abstract_intent import AbstractIntent


class AbstractMeasurementIntent(AbstractIntent):
    sensor_name: str = None
    sensor_key: str = None
    sensor_unit: str = None

    def generate_response(self) -> str:
        module_name, module_index = self._get_module_data()
        sensor_value = self._get_sensor_value(module_index)
        return f"{self.sensor_name} in module {module_name} is {sensor_value} {self.sensor_unit}"

    def _get_sensor_value(self, module_index: int) -> int:
        value = self._get_measurements(module_index, self.sensor_key)
        if value:
            return value
        # TODO: error


class TemperatureIntent(AbstractMeasurementIntent):
    sensor_name = "Water temperature"
    sensor_key = "water_temperature"
    sensor_unit = "degrees Celsius"


class PHIntent(AbstractMeasurementIntent):
    sensor_name = "Water pH"
    sensor_key = "ph"
    sensor_unit = "pH"


class TDSIntent(AbstractMeasurementIntent):
    sensor_name = "Total dissolved solid, TDS, value"
    sensor_key = "tds"
    sensor_unit = "parts per million"


class ECIntent(AbstractMeasurementIntent):
    sensor_name = "Electrical conductivity value"
    sensor_key = "ec"
    sensor_unit = "Ohm meters"

