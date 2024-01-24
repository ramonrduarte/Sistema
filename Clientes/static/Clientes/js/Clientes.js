document.addEventListener('DOMContentLoaded', function () {
    var deleteBtns = document.querySelectorAll('.delete-btn');

    deleteBtns.forEach(function (btn) {
        btn.addEventListener('click', function (event) {
            var ClienteId = btn.getAttribute('data-cliente-id');
            var confirmDeleteBtn = document.getElementById('confirmDeleteBtn');

            confirmDeleteBtn.setAttribute('href', '/excluir/clientes/' + ClienteId);
        });
    });
});