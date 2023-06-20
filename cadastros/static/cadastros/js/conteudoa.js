<script>
$(document).ready(function() {
  function filtrarResultados() {
    var acabamento = $('#id_acabamento').val(); // Obtenha o valor selecionado do acabamento
    var encaixeSim = $('input[name="encaixe"]:checked').val() === '1'; // Verifique se o botão de rádio de encaixe está selecionado como "Sim"

    // Limpe as opções atuais
    var resultadosSelect = $('#idperfilpuxador');
    resultadosSelect.empty();

    // Obtenha os IDs dos perfis de puxador salvos no banco de dados
    var perfilPuxadorIds = resultadosSelect.data('initial-puxador');

    // Adicione as novas opções com base nos resultados filtrados apenas se o botão de rádio estiver selecionado como "Sim"
    if (encaixeSim) {
      $.ajax({
        url: '{% url 'filtrar_acabamento' %}',
        type: 'GET',
        data: {
          acabamento: acabamento
        },
        success: function(response) {
          $.each(response, function(index, item) {
            var checkboxId = 'checkbox_' + item.id;
            var checkboxLabel = $('<label>').attr('for', checkboxId).addClass('form-check-label').text(item.descricao);
            var checkboxInput = $('<input>').attr('type', 'checkbox').attr('name', 'perfil_puxador').attr('id', checkboxId).attr('value', item.id).addClass('form-check-input');

            var checkboxDiv = $('<div>').addClass('form-check').append(checkboxInput, checkboxLabel);
            var option = $('<div>').append(checkboxDiv);

            // Verifique se o perfil de puxador está associado ao perfil sendo editado e marque-o
            if (perfilPuxadorIds && perfilPuxadorIds.includes(item.id.toString())) {
              checkboxInput.prop('checked', true);
            }

            resultadosSelect.append(option);
          });
        },
        error: function(xhr) {
          console.log(xhr.statusText);
        }
      });
    }
  }

  // Chamando a função de filtragem quando o campo de acabamento for alterado
  $('#id_acabamento').change(function() {
    filtrarResultados();
  });

  // Chamando a função de filtragem quando o botão de rádio for alterado
  $('input[name="encaixe"]').change(function() {
    filtrarResultados();
  });

  // Chamando a função de filtragem ao carregar a página para exibir os perfis de puxador salvos
  filtrarResultados();

  // Marcar os checkboxes corretamente ao editar o perfil
  var perfilPuxadorIds = $('#idperfilpuxador').data('initial-puxador');
    if (perfilPuxadorIds) {
      perfilPuxadorIds.forEach(function(id) {
        $('#perfil_puxador_' + id).prop('checked', true);
      });
  }
});

</script>


<script>
$(document).ready(function() {
  function filtrarResultados() {
    var acabamento = $('#id_acabamento').val(); // Obtenha o valor selecionado do acabamento
    var encaixeSim = $('input[name="encaixe"]:checked').val() === '1'; // Verifique se o botão de rádio de encaixe está selecionado como "Sim"

    // Limpe as opções atuais
    var resultadosSelect = $('#idperfilpuxador');
    resultadosSelect.empty();

    // Obtenha os IDs dos perfis de puxador salvos no banco de dados
    var perfilPuxadorIds = resultadosSelect.data('initial-puxador');

    // Adicione as novas opções com base nos resultados filtrados apenas se o botão de rádio estiver selecionado como "Sim"
    if (encaixeSim) {
      $.ajax({
        url: '{% url 'filtrar_acabamento' %}',
        type: 'GET',
        data: {
          acabamento: acabamento
        },
        success: function(response) {
          $.each(response, function(index, item) {
            var checkboxId = 'checkbox_' + item.id;
            var checkboxLabel = $('<label>').attr('for', checkboxId).addClass('form-check-label').text(item.descricao);
            var checkboxInput = $('<input>').attr('type', 'checkbox').attr('name', 'perfil_puxador').attr('id', checkboxId).attr('value', item.id).addClass('form-check-input');

            var checkboxDiv = $('<div>').addClass('form-check').append(checkboxInput, checkboxLabel);
            var option = $('<div>').append(checkboxDiv);

            // Verifique se o perfil de puxador está associado ao perfil sendo editado e marque-o
            if (perfilPuxadorIds && perfilPuxadorIds.includes(item.id.toString())) {
              checkboxInput.prop('checked', true);
            }

            resultadosSelect.append(option);
          });
        },
        error: function(xhr) {
          console.log(xhr.statusText);
        }
      });
    }
  }

  // Chamando a função de filtragem quando o campo de acabamento for alterado
  $('#id_acabamento').change(function() {
    filtrarResultados();
  });

  // Chamando a função de filtragem quando o botão de rádio for alterado
  $('input[name="encaixe"]').change(function() {
    filtrarResultados();
  });

  // Chamando a função de filtragem ao carregar a página para exibir os perfis de puxador salvos
  filtrarResultados();

  // Marcar os checkboxes corretamente ao editar o perfil
  var perfilPuxadorIds = $('#idperfilpuxador').data('initial-puxador');
    if (perfilPuxadorIds) {
      perfilPuxadorIds.forEach(function(id) {
        $('#perfil_puxador_' + id).prop('checked', true);
      });
  }
});


<script>
<!--CONTROLAR PERMITE PERFIL PUXADOR-->
$(document).ready(function() {
  $('input[name="encaixe"]').on('change', function() {
    var valorSelecionado1 = $('input[name="encaixe"]:checked').val();

    // Controlar a primeira div
    if (valorSelecionado1 === '1') {
      $('#idperfilpuxador').show();
    } else {
      $('#idperfilpuxador').clear
      $('#idperfilpuxador').hide();
    }
  });
});
</script>

<script>
<!--CONTROLAR DIVISOR-->
$(document).ready(function() {
  $('input[name="encaixedivisor"]').on('change', function() {
    var valorSelecionado1 = $('input[name="encaixedivisor"]:checked').val();

    // Controlar a primeira div
    if (valorSelecionado1 === '1') {
      $('#iddivisor').show();
    } else {
      $('#iddivisor').clear
      $('#iddivisor').hide();
    }
  });
});
</script>

<script>
<!--CONTROLAR PUXADOR-->
$(document).ready(function() {
  $('input[name="encaixepuxador"]').on('change', function() {
    var valorSelecionado1 = $('input[name="encaixepuxador"]:checked').val();

    // Controlar a primeira div
    if (valorSelecionado1 === '1') {
      $('#idpuxador').show();
    } else {
      $('#idpuxador').clear
      $('#idpuxador').hide();
    }
  });
});
</script>


FUNCIONA INTEIRO

<script>
$(document).ready(function() {
    function filtrarResultados() {
        var acabamento = $('#id_acabamento').val();
        var encaixePerfilPuxadorSim = $('input[name="encaixe"]:checked').val() === '1';
        var encaixeDivisorSim = $('input[name="encaixedivisor"]:checked').val() === '1';
        var encaixePuxadorSim = $('input[name="encaixepuxador"]:checked').val() === '1';

        var resultadosPerfilPuxador = $('#idperfilpuxador');
        var resultadosDivisor = $('#iddivisor');
        var resultadosPuxador = $('#idpuxador');

        resultadosPerfilPuxador.empty();
        resultadosDivisor.empty();
        resultadosPuxador.empty();

        var perfilPuxadorIds = resultadosPerfilPuxador.data('initial-puxador');
        var divisorIds = resultadosDivisor.data('initial-divisor');
        var puxadorIds = resultadosPuxador.data('initial-puxador');

        if (encaixePerfilPuxadorSim) {
            $.ajax({
                url: '{% url 'filtrar_acabamento' %}',
                type: 'GET',
                data: {
                    acabamento: acabamento
                },
                success: function(response) {
                    $.each(response, function(index, item) {
                        var checkboxId = 'checkbox_perfil_puxador_' + item.id;
                        var checkboxLabel = $('<label>').attr('for', checkboxId).addClass('form-check-label').text(item.descricao);
                        var checkboxInput = $('<input>').attr('type', 'checkbox').attr('name', 'perfil_puxador').attr('id', checkboxId).attr('value', item.id).addClass('form-check-input');

                        var checkboxDiv = $('<div>').addClass('form-check').append(checkboxInput, checkboxLabel);
                        var option = $('<div>').append(checkboxDiv);

                        if (perfilPuxadorIds && perfilPuxadorIds.includes(item.id.toString())) {
                            checkboxInput.prop('checked', true);
                        }

                        resultadosPerfilPuxador.append(option);
                    });
                },
                error: function(xhr) {
                    console.log(xhr.statusText);
                }
            });

        } else {
            resultadosPerfilPuxador.hide();
        }

        if (encaixeDivisorSim) {
            $.ajax({
                url: '{% url 'filtrar_divisor' %}',
                type: 'GET',
                data: {
                    acabamento: acabamento
                },
                success: function(response) {
                    $.each(response, function(index, item) {
                        var checkboxId = 'checkbox_divisor_' + item.id;
                        var checkboxLabel = $('<label>').attr('for', checkboxId).addClass('form-check-label').text(item.descricao);
                        var checkboxInput = $('<input>').attr('type', 'checkbox').attr('name', 'divisor').attr('id', checkboxId).attr('value', item.id).addClass('form-check-input');

                        var checkboxDiv = $('<div>').addClass('form-check').append(checkboxInput, checkboxLabel);
                        var option = $('<div>').append(checkboxDiv);

                        if (divisorIds && divisorIds.includes(item.id.toString())) {
                            checkboxInput.prop('checked', true);
                        }

                        resultadosDivisor.append(option);
                    });
                },
                error: function(xhr) {
                    console.log(xhr.statusText);
                }
            });

        } else {
            resultadosDivisor.hide();
        }

        if (encaixePuxadorSim) {
            $.ajax({
                url: '{% url 'filtrar_puxador' %}',
                type: 'GET',
                data: {
                    acabamento: acabamento
                },
                success: function(response) {
                    $.each(response, function(index, item) {
                        var checkboxId = 'checkbox_puxador_' + item.id;
                        var checkboxLabel = $('<label>').attr('for', checkboxId).addClass('form-check-label').text(item.descricao);
                        var checkboxInput = $('<input>').attr('type', 'checkbox').attr('name', 'puxador').attr('id', checkboxId).attr('value', item.id).addClass('form-check-input');

                        var checkboxDiv = $('<div>').addClass('form-check').append(checkboxInput, checkboxLabel);
                        var option = $('<div>').append(checkboxDiv);

                        if (puxadorIds && puxadorIds.includes(item.id.toString())) {
                            checkboxInput.prop('checked', true);
                        }

                        resultadosPuxador.append(option);
                    });
                },
                error: function(xhr) {
                    console.log(xhr.statusText);
                }
            });

        } else {
            resultadosPuxador.hide();
        }
    }

    $('#id_acabamento, input[name="encaixe"], input[name="encaixedivisor"], input[name="encaixepuxador"]').on('change', function() {
        filtrarResultados();
    });

    // Chamar a função filtrarResultados inicialmente
    filtrarResultados();
});

</script>

<script>
$(document).ready(function() {
  $('input[name="encaixe"]').on('change', function() {
    var valorSelecionado1 = $('input[name="encaixe"]:checked').val();

    // Controlar a primeira div
    if (valorSelecionado1 === '1') {
      $('#idperfilpuxador').show();
      $('#iddivisor').empty(); // Limpa a div correspondente ao botão de rádio de divisor
      $('#idpuxador').empty(); // Limpa a div correspondente ao botão de rádio de puxador
    } else {
      if (!$('#idperfilpuxador').is(':hidden')) {
        $('#idperfilpuxador').empty(); // Limpa a div somente se estiver visível
      }
    }
  });
});

$(document).ready(function() {
  $('input[name="encaixedivisor"]').on('change', function() {
    var valorSelecionado1 = $('input[name="encaixedivisor"]:checked').val();

    // Controlar a segunda div
    if (valorSelecionado1 === '1') {
      $('#iddivisor').show();
      $('#idperfilpuxador').empty(); // Limpa a div correspondente ao botão de rádio de perfil puxador
      $('#idpuxador').empty(); // Limpa a div correspondente ao botão de rádio de puxador
    } else {
      if (!$('#iddivisor').is(':hidden')) {
        $('#iddivisor').empty(); // Limpa a div somente se estiver visível
      }
    }
  });
});

$(document).ready(function() {
  $('input[name="encaixepuxador"]').on('change', function() {
    var valorSelecionado1 = $('input[name="encaixepuxador"]:checked').val();

    // Controlar a terceira div
    if (valorSelecionado1 === '1') {
      $('#idpuxador').show();
      $('#idperfilpuxador').empty(); // Limpa a div correspondente ao botão de rádio de perfil puxador
      $('#iddivisor').empty(); // Limpa a div correspondente ao botão de rádio de divisor
    } else {
      if (!$('#idpuxador').is(':hidden')) {
        $('#idpuxador').empty(); // Limpa a div somente se estiver visível
      }
    }
  });
});
</script>