from .abstract_intent import AbstractIntent


class ModuleListIntent(AbstractIntent):

    def generate_response(self) -> str:
        number_of_modules = len(self.response)
        response = f"There are {number_of_modules} modules. "
        response += "Their names are: "
        modules = self._get_module_list()
        response += ", ".join(module["name"] for module in modules) + "."
        return response
