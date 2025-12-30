import reflex as rx
from typing import List
from web.Schemas import RespuesAlumnoExamenCreate,AlumnoCreate
from web.States.AppState import AppState


class ExamenState(AppState):
    
    is_selected_option_bool = False
    selected_options: List[RespuesAlumnoExamenCreate] =[]
    total_preguntas_examen:int=0 

    async def laod_data(self):
        self.preguntas_examen = await self._preguntaController.pregutnas_examen()
        self.total_preguntas_examen = len(self.preguntas_examen) 

    @rx.event
    async def sumbit_response(self,form_data:dict):
        current_alumno = await self._alumnoController.find_cedula(cedula=form_data.get("cedula"))       
        for p in self.selected_options:
            p.alumno_id = current_alumno.id
        await self._examenAlumnoController.create_exam(self.selected_options)
        self.selected_options = []

    @rx.event
    def toggle_optional_selected(self, pregunta_id: int, respuesta_id: int):
        user_response = RespuesAlumnoExamenCreate(alumno_id=0,pregunta_id=pregunta_id,respuesta_id=respuesta_id)
        current =None
        for p in self.selected_options: 
            if p.pregunta_id == pregunta_id and  user_response.respuesta_id == user_response.respuesta_id:
                current = p
                break

        if current: 
            #si es la misma respuesta la eliminamos
            if current.respuesta_id == user_response.respuesta_id:
                self.selected_options.remove(current)
            else:
                #dado que la respuesta es difernte elimnamos la anteior y dejamos la neuva
                self.selected_options.remove(current)
                self.selected_options.append(user_response)
        else:
            #si no existe respuesta agregamos
            self.selected_options.append(user_response)

    @rx.var(cache=False)
    def toggle_optional_submit_button(self)->bool:
        # Habilitar botón solo si todas las preguntas tienen selección
        if self.total_preguntas_examen <=0:
            return True
        total_respuestas = len({p.pregunta_id for p in self.selected_options}) 
        return total_respuestas < self.total_preguntas_examen

    @rx.var(cache=False)
    def is_selected_op(self)->list[str]:
        return [f"{p.pregunta_id}-{p.respuesta_id}" for p in self.selected_options]