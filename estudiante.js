/*document.getElementById("valor").addEventListener("keyup", (e) => {
let pago= $(e.target).val();
 let interes= $("#interes").val();
 let deuda = $("#prestamo").val();
  let numCuota=(pago/(deuda/parseFloat(interes)));
   $("#cuota").val(Number(numCuota.toFixed(1)));//Muestre solamente un decimal 
}); */


// $(document).ready(function () {

//    $('#exampleModal').on("show.bs.modal",(e) => {

//       const form = $(".formulario")[0];
//       if(!form.checkValidity()){
//          e.preventDefault()
//          e.stopPropagation()
//          form.classList.add("was-validated")

//          Swal.fire({
//             icon: "error",
//             title: "Oops...",
//             text:"!debe llenar todos los campos¡"

//           });
//       }

//       let deuda;
//       // let cuotas_pendientes = $("#cuopendiente").val();
//       // let total_pagar = $("#guard").val();
//       // let valor_interes = $("#pagad").val();

//       $("#total_pagar").val() !== '' ? deuda = $("#total_pagar").val() : deuda = $('#valor_prestamo').val();
//       $('#valor_prestamo').val(deuda);
//       $("#valorpre").val(deuda);
//       let interes = $("#interescli").val();
//      $('#inter').val(interes + ' %');

//       $('#pagad').keyup((e) => {
//          let pago = $(e.target).val();
//          calcularPago(pago, deuda, interes)
//              .then(resultado => {
//                  // si la promesa se resulve correctamente, muestra el resultado
//                  $('#cuo').val(resultado.numCuota);
//                  $("#vainter").val(resultado.valor_interes);
//                  $("#paca").val(resultado.pago_Capital);
//                  $("#vaac").val(resultado.valor_pretamo);
//                //   $("#Guardar").click((e) => {
//                //   $("#vaac").val(resultado.valor_pretamo);

//                //   });

//       // $('#pagad').keyup((e) => {
//       //    let pago = $(e.target).val();
//       //    calcularPago(pago, deuda, interes).
//       //       then(resultado => {
//       //          $("#cuo").val(resultado.numCuota);
//       //          $("#vainter").val(resultado.valor_interes);
//       //          $("#paca").val(resultado.pago_Capital);
//       //          $("#Guardar").click((e) => {
//       //             $("#valor_prestamo").val(resultado.valor_prestamo);

//       //          });

//             }).catch(error => {
//                console.error("error al calcular", error);
//             });
//       });
//    });
// });
//    function calcularPago(p, d, i) {

//       return new Promise((resolve, reject) => {
//          let valInt = d / parseFloat(i);
//          let cuota = (p / valInt).toFixed(1);

//             let cuota2 = $("#valorpre").val();
//             let valor_interes = ((p / cuota2) * cuota);
//             let pagoCapital = p - valor_interes;
//             let pago_Capital = d - pagoCapital;
//             let valorActual = d - pago_Capital;

//             if (cuota >= 0) {
//             resolve({
//                numCuota: Number(cuota),
//                valor_interes: (valor_interes),
//                pagoCapital: (pagoCapital),
//                pago_Capital: (pago_Capital),
//                valor_pretamo: (valorActual)

//             });

//          } else { reject('el calculo de la cuota es invalido'); }

//       });
//    }
$(document).ready(function () {
   let fecha;
   $('#fecha_prestamo').change((e) => {

      fecha = $(e.target).val();
      cacularfecha(fecha)
         .then(result => {
            // si la promesa se resulve correctamente, muestra el resultado
            $("#cuotas_pe").val(result.Cuotapendiente);

         }).catch(err => {
            // si la promesa se resulve incorrectamente, muestra el error
            console.error("Error al calcular", err);
         });
   });

   $('#val_pres').keyup((e) => {
      const deuda = parseInt($('#val_pres').val());
      const pendiente = parseInt($('#cuotas_pe').val());
      const interes = parseInt($('#intereses').val());

      const tot = parseFloat(deuda * parseFloat(interes)) / 100;
      $('#total').val(tot);
   });


   $('#modalpagos').on('show.bs.modal', (e) => {

      // $('#botonModal').click((e) => {
      const form = $('.formulario')[0];


      if (!form.checkValidity()) {
         e.preventDefault()//Evita abrir el modal 
         e.stopPropagation()
         form.classList.add('was-validated')

         Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Debe llenar todos los campos!",

         });

         return; //detiene el modal
      } else {
         // const tot = (valor_pres + valor_pres * val_inte / 100 * cuotas_pe);
         let deuda;
         $('#total').val() !== '' ? deuda = $("#total").val() : deuda = $('#val_pres').val();
         $('#prestamo').val(deuda);
         let interes = $("#intereses").val();
         $('#interes').val(interes + ' %');
         let pendiente = $("#cuotas_pe").val();

         $('#valor').keyup((e) => {
            let pago = $(e.target).val();
            calcularPago(pago, deuda, interes, pendiente)
               .then(resultado => {
                  // si la promesa se resulve correctamente, muestra el resultado
                  $('#cuota').val(resultado.numCuota);
                  $("#pago_interes").val(resultado.pagoInteres);
                  $("#pago_capital").val(resultado.pagoCapital);
                  $("#valor_actual").val(resultado.valorActual);

               }).catch(error => {
                  // si la promesa se resulve incorrectamente, muestra el error
                  console.error("Error al calcular", error);

               });
         });
      }


      $("#guardar").click(function () {
         Swal.fire({
            icon: "success",
            title: "!informacion almacenada¡",
            timer: 1500
         }).then(() => {
            let cuota = parseFloat($('#cuota').val());
            let cuota_pend = parseFloat($('#cuota_pe').val());

            if (cuota > cuota_pend) {
               cuota_pend = 0;
               $('#cuota_pe').val(cuota_pend);
            } else {
               cuota_pend = cuota_pend - cuota;
               $('#cuota_pe').val(cuota_pend);
            }
            $('#total').val($('#valor_actual').val());
            $('#modalpagos').modal("hide");
            let modal = $('#modalpagos').find('input');
            modal.each(function () {
               $(this).val('');
            });
         });

      });

   });
});
function calcularPago(p, d, vallnt, pe) {

   return new Promise((resolve, reject) => {

      let valInt = d / parseFloat(vallnt);//para saber el valor de la cuota
      let cuota = (p / valInt).toFixed(1);
      let pago_interes = pe * valInt; // total de interes pagados
      // let capital = p - pago_interes;
      let valActual;
      if (pe !== 0 && cuota <= pe) {
         pago_interes = parseFloat(cuota) * valInt;
         valActual = d - pago_interes;
      } else {
         pago_interes = parseFloat(pe) * valInt;
         valActual = d - p;
      }
      let capital = p - pago_interes;

      if (cuota >= 0) {
         resolve({
            numCuota: Number(cuota),
            pagoCapital: capital,
            pagoInteres: pago_interes,
            valorActual: valActual
         });
      } else {
         reject('El cálculo de la cuota es invalido');
      }
   });
}

function cacularfecha(fec) {
   return new Promise((resolve, reject) => {

      let fecha_pres = new Date(fec);
      let fechaActual = new Date();
      // Calcular la diferencia en años y meses
      let difAnios = fechaActual.getFullYear() - fecha_pres.getFullYear();
      let difMes = fechaActual.getMonth() - fecha_pres.getMonth();
      let difdia = fechaActual.getDate() - fecha_pres.getDate();
      //Si la diferencia de los dias es negativa no ha pasado un mes
      if (difdia <= 0) {
         difMes -= 1;
      }
      let pendiente = (difAnios * 12) + difMes;
      if (pendiente === 0) {
         pendiente = 1;
      }
      resolve({
         Cuotapendiente: pendiente
      });
      reject('El cálculo de la cuota pendiente es invalida.');
   });
}
function limpiar() {
   let modal = $('#modalpagos').find('input');
      modal.each(function () {
         $(this).val('');

      });
};

$('#cerrar'),click(function(){
limpiar();
});
