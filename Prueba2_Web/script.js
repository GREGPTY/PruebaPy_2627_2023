function calcularPerfilRiesgo() {
    // Obtener los datos del formulario
    var nombre = document.getElementById("nombre").value;
    var genero = document.getElementById("genero").value;
    var paisNacimiento = document.getElementById("paisNacimiento").value;
    var paisResidencia = document.getElementById("paisResidencia").value;
    var profesion = document.getElementById("profesion").value;
    var edad = (document.getElementById("edad").value);
    var nivelIngresos = (document.getElementById("nivelIngresos").value);
    var pep = document.getElementById("pep").value;
  
    // Obtener datos adicionales
  
    // Calcular el perfil de riesgo
    var perfilRiesgo = (calcularPuntajeCampoPais(paisNacimiento) * 0.10)+
                       (calcularPuntajeCampoResidencia(paisResidencia) * 0.10) +
                       (calcularPuntajeCampoProfesion(profesion) * 0.20) +
                       (calcularPuntajeCampoEdad(edad) * 0.10) +
                       (calcularPuntajeCampoSalario(nivelIngresos) * 0.20) +
                       (calcularPuntajeCampoPEP(pep) * 0.20);
  
  var perfilRiesgo2 = (calcularPuntajeCampoPais(paisNacimiento))+
                       (calcularPuntajeCampoResidencia(paisResidencia)) +
                       (calcularPuntajeCampoProfesion(profesion)) +
                       (calcularPuntajeCampoEdad(edad)) +
                       (calcularPuntajeCampoSalario(nivelIngresos)) +
                       (calcularPuntajeCampoPEP(pep));
    // Puedes agregar más lógica para el cálculo del perfil de riesgo aquí
  
    // Mostrar el resultado al usuario
    var resultadoDiv = document.getElementById("resultado");
    var perfilRiesgoP = document.getElementById("perfilRiesgo");
    perfilRiesgoP.innerHTML = "Puntaje Total de Riesgo: " + perfilRiesgo;
    resultadoDiv.style.display = "block";
    var resultadoDiv = document.getElementById("resultado2");
    var perfilRiesgo2P = document.getElementById("perfilRiesgo2");
    perfilRiesgo2P.innerHTML = "Puntaje Total de Riesgo: " + perfilRiesgo2 + " el rango es: "+rango(perfilRiesgo2);
    resultadoDiv.style.display = "block";
  }
  function rango(valor){
    if(valor < 1200 ){
      return "bajo";
    }
      else if(valor <= 1400 && valor >= 1200){
        return "medio";
      }
    else if(valor > 1400){
      return "alto";
    }    
  }
  function calcularPuntajeCampoEdad(valor) {
    switch (valor) {
      case "Menos 25":
        return 100;
      case "Entre 25 y 55":
        return 200;
      case "Mayor a 55":
        return 300;
        default:
            return 0;
    }
    }
    function calcularPuntajeCampoSalario(valor){
      switch(valor){
        case "Menosde20Kanual":
        return 100;
      case "Entre20Ky75K":
        return 200;
      case "Mayorde75K":
        return 300;
        default:
            return 0;
    }
    }

    function calcularPuntajeCampoResidencia(valor){
        if(valor == "Panama"){
        return 100;
        }
        else{
            return 200;
        }
    }
    function calcularPuntajeCampoPais(valor){
      if(valor == "Panama"){
      return 100;
      }
      else{
          return 200;
      }
  }
    function calcularPuntajeCampoProfesion(valor){
    switch(valor){
      case "Abogado":
        return 100;
      case "Ingeniero":
        return 200;
      case "Médico":
        return 300;
      case "Contador":
        return 400;
      case "Otras":
        return 500;
        default:
            return 0;
    }
}

function calcularPuntajeCampoPEP(valor){
    switch(valor){  
        case "si":
        return 100;
      case "no":
        return 200;
      default:
        return 0;
    }
  }