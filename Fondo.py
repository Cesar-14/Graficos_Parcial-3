from OpenGL.GL import *

import math
from Modelo import *
import glm

class Fondo(Modelo):
    
    def __init__(self,shader, posicion_id, color_id, transformaciones_id):

        self.vertices = np.array(
            [
                -0.8, 0.8,0.0,1.0,    0.9,1,0.9,1.0,
                0.8, 0.8,0.0,1.0,     0.9,1,0.9,1.0,
                0.8, -0.8,0.0,1.0,    0.9,1,0.9,1.0, 
                -0.8, -0.8,0.0,1.0,   0.9,1,0.9,1.0
                
            ], dtype="float32"
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    -0.8, 0.8,0.0,1.0,    0.9,1,0.9,1.0,
                    0.8, 0.8,0.0,1.0,     0.9,1,0.9,1.0,
                    0.8, -0.8,0.0,1.0,    0.9,1,0.9,1.0, 
                    -0.8, -0.8,0.0,1.0,   0.9,1,0.9,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    -1.1, 0.8,  2.0,1.0,    0.2,1.0,0.7,1.0,
                    -0.5, 0.8,  0.0,1.0,     0.2,1.0,0.7,1.0,
                    -0.5, 0.5, 0.0,1.0,    0.2,1.0,0.7,1.0,
                    -1.1, 0.5, 2.0,1.0,   0.2,1.0,0.7,1.0
                    
                ], dtype="float32"
            )
        )


        #crear una matriz identidad
        self.transformaciones = glm.mat4(1.0)

        super().__init__(shader, posicion_id, color_id, transformaciones_id)

    def dibujar(self):
        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        gl.glUniformMatrix4fv(self.transformaciones_id,
                1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))

        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 2, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 4, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 8, 4)

        gl.glBindVertexArray(0)
        self.shader.liberar_programa()

    def borrar(self):
        gl.glDeleteVertexArrays(1, self.VAO)
        gl.glDeleteBuffers(1, self.VBO)

