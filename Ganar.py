from OpenGL.GL import *
from Modelo import *
import glm

class Ganar(Modelo):

    def __init__(self,shader, posicion_id, transformaciones_id, color_id):
        self.extremo_izquierdo = 0.12
        self.extremo_derecho = 0.12
        self.extremo_inferior = 0.12
        self.extremo_superior = 0.12
        self.posicion = glm.vec3(0.65,-0.65,0.0)

        self.vertices = np.array(
            [
                0.15,  -0.15,0,1.0,   0.2,1.0,0.7,1.0, 
                -0.15, -0.15,0,1.0,  0.2,1.0,0.7,1.0,  
                0.15,  0.15,0,1.0,    0.2,1.0,0.7,1.0,
                -0.15, 0.15,0,1.0,   0.2,1.0,0.7,1.0
            ], dtype="float32"
        )

        self.transformaciones = glm.mat4(1.0)
        super().__init__(shader, posicion_id, transformaciones_id, color_id)

    def actualizar(self,tiempo_delta):
        cantidad_movimiento = tiempo_delta
    
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
