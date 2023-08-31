// gira porta conforme calculo de largura x altura
function rotacionarGrupo() {
    var grupoVidro = document.getElementById('Desenho');
    var largura = parseFloat($('#id_largura').val());
    var altura = parseFloat($('#id_altura').val());

    grupoVidro.style.transformBox = 'fill-box';
    grupoVidro.style.transformOrigin = 'center center';

    var angle = (largura > altura) ? -90 : 0;

    anime({
        targets: grupoVidro,
        rotate: angle,
        duration: 1000,
        easing: 'easeInOutQuad'
    });

    updateAnimation();

    updateMedidas(largura, altura);
// mostra barra de medidas caso tenha valores nos campos
    if (!isNaN(largura) && !isNaN(altura)) {
        var medidaDesenho = document.getElementById('MedidaDesenho');
        medidaDesenho.classList.remove('st2');
        medidaDesenho.classList.add('st6');
    } else {
        var medidaDesenho = document.getElementById('MedidaDesenho');
        medidaDesenho.classList.remove('st6');
        medidaDesenho.classList.add('st2');
    }
}

// atualiza valor de medidas
function updateMedidas(largura, altura) {
    var medidaLargura = document.getElementById('Medida-A'); // Alterado para Medida-A
    var medidaAltura = document.getElementById('Medida-B'); // Alterado para Medida-B

    if (altura >= largura) {
        medidaLargura.textContent = largura + "mm";
        medidaAltura.textContent = altura + "mm";
    } else {
        medidaLargura.textContent = altura + "mm";
        medidaAltura.textContent = largura + "mm";
    }
}

function updateAnimation() {
    const largura = parseFloat($('#id_largura').val());
    const altura = parseFloat($('#id_altura').val());

    const targets = [
        // ... (mantenha os objetos como estão)
    ];

    targets.forEach(({ target, initialPoints, finalPoints }) => {
        const points = (largura > altura) ? finalPoints : initialPoints;
        animateSVGTargets(target, initialPoints, points);
    });
}

$(document).ready(function() {
    $('#id_largura, #id_altura').on('blur', function() {
        rotacionarGrupo();
    });
});


$(document).ready(function() {

  function atualizarClassePerfil() {
    var idPerfilElement = document.getElementById('id_perfil');
    var perfisElement = document.getElementById('Perfis');
    var acabElement = document.getElementById('Acabamento');

    var selectedValue = idPerfilElement.value;

    if (selectedValue !== '') {
      perfisElement.setAttribute('class', 'st6');
      acabElement.setAttribute('class', 'st6');
    } else {
      perfisElement.setAttribute('class', 'st2');
      acabElement.setAttribute('class', 'st2');
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

  filtrarPerfil();
});
