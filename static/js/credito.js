  function calcularCotizacion() {
    const cantidad = parseFloat(document.getElementById("cantidad").value);
    const buro = document.getElementById("buro").value;
    const mensualidadSeleccionada = document.querySelector('input[name="mensualidades"]:checked');
    const resultado = document.getElementById("resultado-cotizacion");

    resultado.innerHTML = "";

    if (!cantidad || cantidad < 50000) {
      Swal.fire({
        icon: "warning",
        title: "Monto no válido",
        text: "El monto del crédito debe ser mayor o igual a $50,000 MXN.",
        confirmButtonText: "Entendido",
        confirmButtonColor: "#8b0d24"
      });
      return;
    }

    if (!mensualidadSeleccionada) {
      Swal.fire({
        icon: "info",
        title: "Selecciona un plazo",
        text: "Debes seleccionar el número de mensualidades para calcular la cotización.",
        confirmButtonText: "Aceptar",
        confirmButtonColor: "#8b0d24"
      });
      return;
    }

    const meses = parseInt(mensualidadSeleccionada.value);

    let tasaAnual = 0.18;

    if (buro === "regular") {
      tasaAnual = 0.24;
    } else if (buro === "malo") {
      tasaAnual = 0.32;
    }

    const tasaMensual = tasaAnual / 12;

    const pagoMensual = cantidad *
      (tasaMensual * Math.pow(1 + tasaMensual, meses)) /
      (Math.pow(1 + tasaMensual, meses) - 1);

    const totalPagar = pagoMensual * meses;
    const intereses = totalPagar - cantidad;

    resultado.innerHTML = `
      <div class="alert alert-success rounded-4 shadow-sm">
        <h5 class="fw-bold mb-3">Resultado aproximado</h5>

        <p class="mb-2">
          <strong>Monto solicitado:</strong> 
          $${cantidad.toLocaleString("es-MX", { minimumFractionDigits: 2 })}
        </p>

        <p class="mb-2">
          <strong>Plazo:</strong> ${meses} meses
        </p>

        <p class="mb-2">
          <strong>Buró de crédito:</strong> ${buro}
        </p>

        <hr>

        <p class="fs-5 mb-2">
          <strong>Pago mensual aproximado:</strong>
          $${pagoMensual.toLocaleString("es-MX", { minimumFractionDigits: 2 })}
        </p>

        <p class="mb-1">
          <strong>Total aproximado a pagar:</strong>
          $${totalPagar.toLocaleString("es-MX", { minimumFractionDigits: 2 })}
        </p>

        <p class="mb-0 text-muted">
          <strong>Intereses aproximados:</strong>
          $${intereses.toLocaleString("es-MX", { minimumFractionDigits: 2 })}
        </p>
      </div>
    `;
  }

  document.addEventListener("DOMContentLoaded", function () {

    const botones = document.querySelectorAll(".tab-btn");
    const cards = document.querySelectorAll(".car-card");

    function mostrarCategoria(categoria) {

        // Ocultar todas
        cards.forEach(card => card.style.display = "none");

        let visibles = [];

        cards.forEach(card => {

            const tipo = card.dataset.tipo.toLowerCase();

            if (categoria === "destacados") {
                visibles.push(card);
            }
            else if (categoria === "sedan" && tipo === "sedan") {
                visibles.push(card);
            }
            else if (categoria === "suv" && tipo === "suv") {
                visibles.push(card);
            }
            else if (categoria === "pic-kup" && (tipo === "pic-kup" || tipo === "pick-up")) {
                visibles.push(card);
            }
            else if (categoria === "seminuevo" && tipo === "seminuevo") {
                visibles.push(card);
            }

        });

        // Mostrar únicamente los primeros 4
        visibles.slice(0, 4).forEach(card => {
            card.style.display = "block";
        });
    }

    // Mostrar 8 destacados al cargar la página
    mostrarCategoria("destacados");

    botones.forEach(boton => {

        boton.addEventListener("click", function () {

            botones.forEach(btn => btn.classList.remove("active"));
            this.classList.add("active");

            mostrarCategoria(this.dataset.tab);

        });

    });

});

/*Catalogo filtrado*/
document.addEventListener("DOMContentLoaded", function () {
  const tabs = document.querySelectorAll(".catalogo-tab");
  const cards = document.querySelectorAll(".catalogo-card");

  tabs.forEach(tab => {
    tab.addEventListener("click", function () {
      const filtro = this.dataset.filter;

      tabs.forEach(t => t.classList.remove("active"));
      this.classList.add("active");

      cards.forEach(card => {
        const tipo = card.dataset.tipo;

        if (filtro === "todos" || tipo === filtro) {
          card.style.display = "block";
        } else {
          card.style.display = "none";
        }
      });
    });
  });
});

