
$(document).ready(function() {

  function atualizarClassePerfil() {
    var idPerfilElement = document.getElementById('id_perfil');
    var perfisElement = document.getElementById('Perfis');
    var selectedValue = idPerfilElement.value;

    if (selectedValue !== '') {
      perfisElement.setAttribute('class', 'st6');
    } else {
      perfisElement.setAttribute('class', 'st2');
    }
  }

  function observarCampoPerfil() {
    var perfilObserver = new MutationObserver(function(mutationsList) {
      for (var mutation of mutationsList) {
        if (mutation.type === 'childList' && mutation.target.id === 'id_perfil') {
          atualizarClassePerfil();
          break;
        }
      }
    });

    perfilObserver.observe(document.getElementById('id_perfil'), { childList: true });
  }

  $('#id_perfil').change(atualizarClassePerfil);

  observarCampoPerfil();


});



