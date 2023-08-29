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

    if (!isNaN(largura) && !isNaN(altura)) {
        var medidaDesenho = document.getElementById('MedidaDesenho');
        var Perfis = document.getElementById('Perfis');
        medidaDesenho.classList.remove('st2'); // Remove a classe st2
        medidaDesenho.classList.add('st6');    // Adiciona a classe st6
        Perfis.classList.remove('st2'); // Remove a classe st2
        Perfis.classList.add('st6');    // Adiciona a classe st6
    } else {
        var medidaDesenho = document.getElementById('MedidaDesenho');
        var Perfis = document.getElementById('Perfis');
        medidaDesenho.classList.remove('st6'); // Remove a classe st6
        medidaDesenho.classList.add('st2');    // Adiciona a classe st2
        Perfis.classList.remove('st6'); // Remove a classe st6
        Perfis.classList.add('st2');    // Adiciona a classe st2
    }
}

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

function atualizarClassePerfil() {
    var campoId = document.getElementById('divperfil');
    var svgDoc = document.getElementById('svg').contentDocument; // Substitua 'seu-svg-id' pelo ID do elemento <svg> que contém o elemento 'Perfis'
    var elementoPerfil = svgDoc.getElementById('Perfis');

    if (campoId.value !== "") {
        elementoPerfil.classList.remove('st2');
        elementoPerfil.classList.add('st6');
    } else {
        elementoPerfil.classList.remove('st6');
        elementoPerfil.classList.add('st2');
    }
}

// Adicione um ouvinte de eventos ao campo divperfil
var campoDivPerfil = document.getElementById('divperfil');
campoDivPerfil.addEventListener('input', atualizarClassePerfil);

