import reflex as rx
from typing import Dict, Optional


class IndexState(rx.State):
    disabled_submit_button: bool = True
    is_selected_option_bool = False

    selected_options: Dict[int, Optional[int]] = {}

    @rx.event
    def toggle_optional_selected(self, pregunta_id: int, respuesta_id: int):
        current = self.selected_options.get(pregunta_id)
        if current == respuesta_id:
            # desmarcar si ya estaba seleccionada
            self.selected_options[pregunta_id] = None
        else:
            self.selected_options[pregunta_id] = respuesta_id
        self.is_selected_option_bool = not (self.is_selected_option_bool)
        print( self.selected_options)



    @rx.event
    def toggle_optional_submit_button(self):
        # Habilitar botón solo si todas las preguntas tienen selección
        self.disabled_submit_button = not all(
            resp is not None for resp in self.selected_options.values()
        )
        # self.disabled_submit_button = not (self.disabled_submit_button)

    async def laod_data(self):
        pass
