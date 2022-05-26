from OpenGL.GL import *
from Modelo import *
import glm

class Enemigo5(Modelo):

    velocidad = 3
    direccion = 0

    def __init__(self,shader, posicion_id, transformaciones_id, color_id):
        self.extremo_izquierdo = 0.07
        self.extremo_derecho = 0.07
        self.extremo_inferior = 0.0
        self.extremo_superior = 0.0
        self.posicion = glm.vec3(-0.3,-0.05,0.0)

        self.vertices = np.array(
            [
                0.055, 0.125,0,1.0,   0.2,0.2,0.9,1.0, 
                -0.055, 0.125,0,1.0,  0.2,0.2,0.9,1.0,  
                0.055, 0.01,0,1.0,    0.2,0.2,0.9,1.0,
                -0.055, 0.01,0,1.0,   0.2,0.2,0.9,1.0
            ], dtype="float32"
        )

        self.transformaciones = glm.mat4(1.0)
        super().__init__(shader, posicion_id, transformaciones_id, color_id)

    def actualizar(self,tiempo_delta):
        cantidad_movimiento = self.velocidad * tiempo_delta
        if self.direccion == 0:
            self.posicion.y = self.posicion.y - cantidad_movimiento
        elif self.direccion == 1:
            self.posicion.y = self.posicion.y + cantidad_movimiento
        if self.posicion.y <= -0.8 and self.direccion == 0:
            self.direccion = 1
        if self.posicion.y >= 0.7 and self.direccion == 1:
            self.direccion = 0
    
    def dibujar(self):

        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones, self.posicion)

    
        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        gl.glUniformMatrix4fv(self.transformaciones_id,
            1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))


        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)

        gl.glBindVertexArray(0)
        self.shader.liberar_programa()