<script>
function updatePerfilPuxDireita() {
    const groupId = "PerfilPux_Direita_1_";
    const gradientTransform = "matrix(1 0 0 1 286.573 138.9768)";
    const polylinePoints = "193,104.8 197.7,104.8 197.7,254.3 193,254.3";
    const rectX = "197.7";
    const rectY = "104.7";
    const rectWidth = "1.7";
    const rectHeight = "149.6";

    const group = document.getElementById(groupId);
    if (!group) {
        console.error("Group not found.");
        return;
    }

    const linearGradient = group.querySelector("linearGradient");
    const polyline = group.querySelector("polyline");
    const rect = group.querySelector("rect");

    if (linearGradient) {
        linearGradient.setAttribute("gradientTransform", gradientTransform);
    }

    if (polyline) {
        polyline.setAttribute("points", polylinePoints);
    }

    if (rect) {
        rect.setAttribute("x", rectX);
        rect.setAttribute("y", rectY);
        rect.setAttribute("width", rectWidth);
        rect.setAttribute("height", rectHeight);
    }
}
</script>

<script>
function rotacionarGrupo() {
    var grupoVidro = document.getElementById('Vidro');
    var grupoAcabamento = document.getElementById('Acabamento');

    // Define o ponto de rotação no centro do grupo
    grupoVidro.style.transformBox = 'fill-box';
    grupoVidro.style.transformOrigin = 'center center';
    grupoAcabamento.style.transformBox = 'fill-box';
    grupoAcabamento.style.transformOrigin = 'center center';

    // Cria a animação usando Anime.js para o grupo Vidro
    anime({
        targets: grupoVidro,
        rotate: -90,
        duration: 1000, // Duração da animação em milissegundos
        easing: 'easeInOutQuad' // Efeito de easing da animação
    });

    // Cria a animação usando Anime.js para o grupo Acabamento
    anime({
        targets: grupoAcabamento,
        rotate: -90,
        duration: 1000, // Duração da animação em milissegundos
        easing: 'easeInOutQuad' // Efeito de easing da animação
    });
}

document.getElementById('btnpedidofinalizar').addEventListener('click', function() {
    rotacionarGrupo();
});
</script>

<script>
function animateSVGTargets(target, initialPoints, finalPoints) {
    anime({
        targets: target,
        points: [
            { value: initialPoints },
            { value: finalPoints }
        ],
        easing: 'easeInOutQuad',
        duration: 2000,
    });
}

function updateAnimation() {
    const largura = parseFloat($('#id_largura').val());
    const altura = parseFloat($('#id_altura').val());

    const targets = [
        {
            target: '#Perf-Direita',
            initialPoints: '141.7,68 141.7,282.7 152.7,293.7 152.7,57',
            finalPoints: '182,115.7 182,243.3 193,254.3 193,104.7'
        },
        {
            target: '#Perf-Superior',
            initialPoints: '152.7,57 3.1,57 14.1,68 141.7,68',
            finalPoints: '-32.7,115.7 182,115.7 193,104.7 -43.7,104.7'
        },
        {
            target: '#Perf-Esquerda',
            initialPoints: '3.1,57 3.1,293.7 14.1,282.7 14.1,68',
            finalPoints: '-43.7,104.7 -43.7,254.3 -32.7,243.3 -32.7,115.7'
        },
        {
            target: '#Perf-Inferior',
            initialPoints: '141.7,282.7 14.1,282.7 3.1,293.7 152.7,293.7',
            finalPoints: '-43.7,254.3 193,254.3 182,243.3 -32.7,243.3'
        },
    ];

    targets.forEach(({ target, initialPoints, finalPoints }) => {
        const points = (largura > altura) ? finalPoints : initialPoints;
        animateSVGTargets(target, initialPoints, points);
    });
}

$(document).ready(function() {
    $('#id_largura, #id_altura').on('blur', updateAnimation);
});
</script>