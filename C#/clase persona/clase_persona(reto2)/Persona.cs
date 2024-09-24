using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace clase_persona_reto2_
{
    internal class Persona
    {
        public string Nombre { get; set; }
        public string Apellido { get; set; }
        public int Edad { get; set; }

        public Persona( string nombre , string apellido , int edad) {

            Nombre = nombre;
            Apellido = apellido;
            Edad = edad;
        }

        public void Saludar ()
        {
            Console.WriteLine("saludos {0} de apellido {1} como estas", Nombre, Apellido);
        }
    }
}
