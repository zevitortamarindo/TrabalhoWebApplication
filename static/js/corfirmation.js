(function () {

    const btnConfirmation = document.querySelectorAll(".btnConfirmation");

    btnConfirmation.forEach(btn => {
        btn.addEventListener("click", (e) => {
            const confirmation = confirm("Tem certeza que deseja excluir essa música?");
            if(!confirmation) {
                e.preventDefault();
            }
        });
    });
})();