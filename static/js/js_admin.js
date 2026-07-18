const precio = document.getElementById('precio_unidad');

precio.addEventListener('input', function(e) {

    // Elimina todo lo que no sea número
    let valor = e.target.value.replace(/\D/g, '');

    if(valor === ''){
        e.target.value = '';
        return;
    }

    // Agrega separadores de miles
    e.target.value = Number(valor).toLocaleString('es-MX');

});

// Antes de enviar el formulario elimina las comas
precio.form.addEventListener('submit', function(){

    precio.value = precio.value.replace(/,/g,'');

});
document.addEventListener("DOMContentLoaded", function () {

  const tabs = document.querySelectorAll(".catalogo-tab");
  const grid = document.querySelector(".catalogo-grid");
  const selectOrden = document.getElementById("ordenPrecio");
  const cardsOriginales = Array.from(document.querySelectorAll(".catalogo-card"));

  let filtroActual = "todos";

  function obtenerPrecio(card) {
    let precio = card.getAttribute("data-precio") || "0";

    precio = precio.replace(/[^\d.]/g, "");

    return parseFloat(precio) || 0;
  }

  function mostrarCatalogo() {
    const orden = selectOrden.value;

    let cardsFiltradas = cardsOriginales.filter(card => {
      const tipo = (card.getAttribute("data-tipo") || "").trim().toLowerCase();
      return filtroActual === "todos" || tipo === filtroActual;
    });

    if (orden === "menor-mayor") {
      cardsFiltradas.sort((a, b) => obtenerPrecio(a) - obtenerPrecio(b));
    }

    if (orden === "mayor-menor") {
      cardsFiltradas.sort((a, b) => obtenerPrecio(b) - obtenerPrecio(a));
    }

    if (orden === "destacados") {
      cardsFiltradas.sort((a, b) => cardsOriginales.indexOf(a) - cardsOriginales.indexOf(b));
    }

    grid.innerHTML = "";

    cardsFiltradas.forEach(card => {
      grid.appendChild(card);
    });
  }

  tabs.forEach(tab => {
    tab.addEventListener("click", function () {
      filtroActual = this.dataset.filter.trim().toLowerCase();

      tabs.forEach(t => t.classList.remove("active"));
      this.classList.add("active");

      mostrarCatalogo();
    });
  });

  selectOrden.addEventListener("change", mostrarCatalogo);

  mostrarCatalogo();

});

document.addEventListener("DOMContentLoaded", function () {
    const modalCotizacion = document.getElementById('modalCotizacion');

    if (modalCotizacion) {
        modalCotizacion.addEventListener('show.bs.modal', function (event) {
            const boton = event.relatedTarget;

            document.getElementById('modalIdAuto').value = boton.getAttribute('data-id');

            document.getElementById('modalAutoTexto').innerHTML = `
                <strong>
                    ${boton.getAttribute('data-marca')}
                    ${boton.getAttribute('data-modelo')}
                    ${boton.getAttribute('data-anio')}
                </strong><br>
                <span class="text-success fw-bold">
                    Desde $${boton.getAttribute('data-precio')}
                </span>
            `;
        });
    }
});

const telefono = document.getElementById("celular_cliente");

telefono.addEventListener("input", function () {

    // Elimina cualquier carácter que no sea un número
    this.value = this.value.replace(/\D/g, "");

    // Limita a 10 dígitos
    if (this.value.length > 10) {
        this.value = this.value.slice(0, 10);
    }

});
document.querySelector("form").addEventListener("submit", function(e) {

    const telefono = document.getElementById("celular_cliente");

    if (telefono.value.length !== 10) {
        e.preventDefault();

        Swal.fire({
            icon: "warning",
            title: "Número inválido",
            text: "El teléfono debe contener exactamente 10 dígitos."
        });

        telefono.focus();
    }

});
document.addEventListener("input", function (e) {
    if (e.target.classList.contains("solo-numeros")) {
        e.target.value = e.target.value.replace(/[^0-9]/g, "").slice(0, 10);
    }
});


setInterval(actualizarGraficas,5000);

async function actualizarGraficas(){

    const respuesta=await fetch("/api/reporte_vehiculos");

    const datos=await respuesta.json();

    graficaMasVendidos.data.labels=datos.labelsMas;
    graficaMasVendidos.data.datasets[0].data=datos.valoresMas;
    graficaMasVendidos.update();

    graficaMenosVendidos.data.labels=datos.labelsMenos;
    graficaMenosVendidos.data.datasets[0].data=datos.valoresMenos;
    graficaMenosVendidos.update();

}

    document.addEventListener("DOMContentLoaded", function () {

        if (!document.getElementById("tablaAutos")) {
            return;
        }

        if ($.fn.DataTable.isDataTable("#tablaAutos")) {
            $("#tablaAutos").DataTable().destroy();
        }

        $("#tablaAutos").DataTable({

            responsive: true,
            autoWidth: false,
            scrollX: true,

            // Máximo de cinco registros por página
            pageLength: 5,
            lengthChange: false,

            order: [[0, "desc"]],

            dom:
                "<'row align-items-center mb-3'<'col-lg-7 col-md-12'B><'col-lg-5 col-md-12'f>>" +
                "<'row'<'col-12'tr>>" +
                "<'row align-items-center mt-3'<'col-md-6'i><'col-md-6'p>>",

            buttons: [
                
                {
                    extend: "pdfHtml5",
                    text: "📄 PDF",
                    className: "btn btn-danger btn-sm lg-5",
                    title: "Catálogo de vehículos",
                    orientation: "landscape",
                    pageSize: "A4",
                    exportOptions: {
                        columns: ":not(:last-child)"
                    }
                }
                
                
                
            ],

            language: {
                search: "Buscar:",
                searchPlaceholder: "Marca, modelo, tipo...",
                emptyTable: "No hay vehículos registrados",
                zeroRecords: "No se encontraron vehículos",
                info: "Mostrando _START_ a _END_ de _TOTAL_ vehículos",
                infoEmpty: "Mostrando 0 vehículos",
                infoFiltered: "(filtrado de _MAX_ registros)",
                loadingRecords: "Cargando...",
                processing: "Procesando...",
                paginate: {
                    first: "Primero",
                    last: "Último",
                    next: "Siguiente",
                    previous: "Anterior"
                }
            },

            columnDefs: [
                {
                    targets: [1, 8],
                    orderable: false,
                    searchable: false
                },
                {
                    targets: 8,
                    className: "text-center"
                }
            ]
        });

    });

document.addEventListener("DOMContentLoaded", function () {

    const modalSolicitud =
        document.getElementById("modalSolicitudCredito");

    const formulario =
        document.getElementById("formSolicitudCredito");

    const telefono =
        document.getElementById("telefonoSolicitud");

    const monto =
        document.getElementById("montoSolicitud");

    const botonGuardar =
        document.getElementById("btnGuardarSolicitud");


    if (
        !modalSolicitud ||
        !formulario ||
        !telefono ||
        !monto
    ) {
        return;
    }


    /* ==========================================
       VALIDAR TELÉFONO
    ========================================== */

    telefono.addEventListener("input", function () {

        this.value = this.value
            .replace(/\D/g, "")
            .slice(0, 10);
    });


    /* ==========================================
       FORMATEAR MONTO
    ========================================== */

    monto.addEventListener("input", function () {

        const valorNumerico =
            this.value.replace(/\D/g, "");

        if (valorNumerico === "") {
            this.value = "";
            return;
        }

        this.value = Number(
            valorNumerico
        ).toLocaleString("es-MX");
    });


    /* ==========================================
       VALIDAR Y ENVIAR FORMULARIO
    ========================================== */

    formulario.addEventListener("submit", function (evento) {

        const telefonoLimpio =
            telefono.value.replace(/\D/g, "");

        const montoLimpio =
            monto.value.replace(/,/g, "");

        const montoNumerico =
            Number(montoLimpio);


        if (!formulario.checkValidity()) {

            evento.preventDefault();
            evento.stopPropagation();

            formulario.classList.add("was-validated");

            Swal.fire({
                icon: "warning",
                title: "Información incompleta",
                text: "Completa correctamente todos los campos obligatorios.",
                confirmButtonText: "Aceptar",
                confirmButtonColor: "#0d6efd"
            });

            return;
        }


        if (telefonoLimpio.length !== 10) {

            evento.preventDefault();

            Swal.fire({
                icon: "warning",
                title: "Teléfono inválido",
                text: "El teléfono debe contener exactamente 10 dígitos.",
                confirmButtonText: "Aceptar",
                confirmButtonColor: "#0d6efd"
            });

            telefono.focus();

            return;
        }


        if (
            !Number.isFinite(montoNumerico) ||
            montoNumerico < 50000
        ) {

            evento.preventDefault();

            Swal.fire({
                icon: "warning",
                title: "Monto inválido",
                text: "El monto solicitado debe ser de al menos $50,000.00 MXN.",
                confirmButtonText: "Aceptar",
                confirmButtonColor: "#0d6efd"
            });

            monto.focus();

            return;
        }


        // Enviar teléfono y monto sin separadores

        telefono.value = telefonoLimpio;
        monto.value = montoLimpio;

        botonGuardar.disabled = true;

        botonGuardar.innerHTML = `
            <span class="spinner-border spinner-border-sm me-2"></span>
            Guardando...
        `;
    });


    /* ==========================================
       LIMPIAR MODAL AL CERRAR
    ========================================== */

    modalSolicitud.addEventListener(
        "hidden.bs.modal",
        function () {

            formulario.reset();

            formulario.classList.remove(
                "was-validated"
            );

            botonGuardar.disabled = false;

            botonGuardar.innerHTML = `
                <i class="fa-solid fa-floppy-disk me-1"></i>
                Guardar solicitud
            `;
        }
    );

});
