// Mostrar/Ocultar contraseña
    function togglePassword() {

        const password = document.getElementById("password");
        const eyeIcon = document.getElementById("eyeIcon");

        if(password.type === "password"){
            password.type = "text";
            eyeIcon.classList.replace("bi-eye","bi-eye-slash");
        }else{
            password.type = "password";
            eyeIcon.classList.replace("bi-eye-slash","bi-eye");
        }
    }

    // Validaciones Bootstrap
    (() => {
        'use strict'

        const forms = document.querySelectorAll('.needs-validation')

        Array.from(forms).forEach(form => {

            form.addEventListener('submit', event => {

                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                }

                form.classList.add('was-validated')

            }, false)

        })

    })();
