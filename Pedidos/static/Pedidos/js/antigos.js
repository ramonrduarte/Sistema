<script>
document.addEventListener("DOMContentLoaded", function() {

    //Escolha de div conforme o modelo de porta
    const radioButtons = document.querySelectorAll('input[type="radio"][name="btnradio"]');
    const divportas = document.getElementById("divportas");
    const divambiente = document.getElementById("divambiente");
    const divvidros = document.getElementById("divvidros");
    const divacabamento = document.getElementById("divacabamento");
    const divabertura = document.getElementById("divabertura");
    const divlinha = document.getElementById("divlinha");


    radioButtons.forEach(radio => {
      radio.addEventListener('change', function() {
        if (this.value === 'PortaGiro' || this.value === 'PortaCorrer') {
          divportas.style.display = "block";
          divambiente.style.display = "none";
          divvidros.style.display = "none";
          divacabamento.style.display = "block";
          divabertura.style.display = "block";
          divlinha.style.display = "none";
        } else if (this.value === 'DivisoriaAmbiente') {
          divportas.style.display = "none";
          divambiente.style.display = "block";
          divvidros.style.display = "none";
          divacabamento.style.display = "block";
          divabertura.style.display = "none";
          divlinha.style.display = "block";
        } else if (this.value === 'Vidros') {
          divportas.style.display = "none";
          divambiente.style.display = "none";
          divvidros.style.display = "block";
          divacabamento.style.display = "none";
          divabertura.style.display = "none";
          divlinha.style.display = "none";
        }
      });
    });

</script>

<!--<script>-->
<!--$(document).ready(function() {-->
<!--    $('#id_perfil').select2();-->
<!--});-->
<!--</script>-->



<script>
$(document).ready(function() {
  $('#id_acabamento').change(function() {
    filtrarPerfil();
  });

  function filtrarPerfil() {
    var acabamento = $('#id_acabamento').val();

    if (acabamento) {
      $.ajax({
        url: '/filtrar_acabamento/',  // Atualize para a URL correta
        type: 'GET',
        data: {
          acabamento: acabamento
        },
        success: function(response) {
          var selectPerfil = $('#id_perfil');
          selectPerfil.empty();

          var option = $('<option>').attr('value', '').text('-------');
          selectPerfil.append(option);

          $.each(response, function(index, item) {
            option = $('<option>').attr('value', item.id).text(item.descricao);
            selectPerfil.append(option);
          });

          selectPerfil.show();
        },
        error: function(xhr) {
          console.log(xhr.statusText);
        }
      });
    } else {
      $('#id_perfil').empty();
    }
  }
});
</script>

<script>
$(document).ready(function() {
  $('#id_perfil').change(function() {
    buscarPerfilPuxador();
  });

  function buscarPerfilPuxador() {
    var perfil = $('#id_perfil').val();

    if (perfil) {
      $.ajax({
        url: '/buscar_PerfilPuxador/',  // Atualize para a URL correta
        type: 'GET',
        data: {
          perfil: perfil
        },
        success: function(response) {
          var selectPerfilPuxador = $('#id_perfilpuxador');
          selectPerfilPuxador.empty();

          var option = $('<option>').attr('value', '').text('-------');
          selectPerfilPuxador.append(option);

          $.each(response, function(index, item) {
            option = $('<option>').attr('value', item.id).text(item.descricao);
            selectPerfilPuxador.append(option);
          });

          // Verificar o número de itens na resposta
          var numItens = response.length;

          // Desabilitar ou habilitar o campo divisor com base no número de itens
          if (numItens <= 0) {
            selectPerfilPuxador.prop('disabled', true);
            $('#divperfilpuxador :input').prop('disabled', true); // Bloquear campos dentro da div com id="divperfilpuxador"
          } else {
            selectPerfilPuxador.prop('disabled', false);
            $('#divperfilpuxador :input').prop('disabled', false); // Desbloquear campos dentro da div com id="divperfilpuxador"
          }

          selectPerfilPuxador.show();
        },
        error: function(xhr) {
          console.log(xhr.statusText);
        }
      });
    } else {
      $('#id_perfilpuxador').empty();
      $('#divperfilpuxador :input').prop('disabled', true); // Bloquear campos dentro da div com id="divpuxador"
    }
  }
});
</script>

<script>
$(document).ready(function() {
  $('#id_perfil').change(function() {
    buscarDivisor();
    limparCampoVidro(); // Adicionado chamada para a função limparCampoVidro()
  });

  function buscarDivisor() {
    var perfil = $('#id_perfil').val();

    if (perfil) {
      $.ajax({
        url: '/buscar_Divisor/',  // Atualize para a URL correta
        type: 'GET',
        data: {
          perfil: perfil
        },
        success: function(response) {
          var selectDivisor = $('#id_divisor');
          selectDivisor.empty();

          var option = $('<option>').attr('value', '').text('-------');
          selectDivisor.append(option);

          $.each(response, function(index, item) {
            option = $('<option>').attr('value', item.id).text(item.descricao);
            selectDivisor.append(option);
          });

          // Verificar o número de itens na resposta
          var numItens = response.length;

          // Desabilitar ou habilitar o campo divisor com base no número de itens
          if (numItens <= 0) {
            selectDivisor.prop('disabled', true);
            $('#divdivisor :input').prop('disabled', true); // Bloquear campos dentro da div com id="divdivisor"
          } else {
            selectDivisor.prop('disabled', false);
            $('#divdivisor :input').prop('disabled', false); // Desbloquear campos dentro da div com id="divdivisor"
          }

          selectDivisor.show();
        },
        error: function(xhr) {
          console.log(xhr.statusText);
        }
      });
    } else {
      $('#id_divisor').empty();
      $('#divdivisor :input').prop('disabled', true); // Bloquear campos dentro da div com id="divdivisor"
    }
  }

  // Função para limpar o campo id_vidro
  function limparCampoVidro() {
    $('#id_vidro').val('');
  }
});

</script>

<script>
$(document).ready(function() {
  $('#id_perfil').change(function() {
    buscarPuxador();
  });

  function buscarPuxador() {
    var perfil = $('#id_perfil').val();

    if (perfil) {
      $.ajax({
        url: '/buscar_Puxador/',  // Atualize para a URL correta
        type: 'GET',
        data: {
          perfil: perfil
        },
        success: function(response) {
          var selectPuxador = $('#id_puxador');
          selectPuxador.empty();

          var option = $('<option>').attr('value', '').text('-------');
          selectPuxador.append(option);

          $.each(response, function(index, item) {
            option = $('<option>').attr('value', item.id).text(item.descricao);
            selectPuxador.append(option);
          });

          // Verificar o número de itens na resposta
          var numItens = response.length;

          // Desabilitar ou habilitar o campo puxador com base no número de itens
          if (numItens <= 0) {
            selectPuxador.prop('disabled', true);
            $('#divpuxador :input').prop('disabled', true); // Bloquear campos dentro da div com id="divpuxador"
          } else {
            selectPuxador.prop('disabled', false);
            $('#divpuxador :input').prop('disabled', false); // Desbloquear campos dentro da div com id="divpuxador"
          }

          selectPuxador.show();
        },
        error: function(xhr) {
          console.log(xhr.statusText);
        }
      });
    } else {
      $('#id_puxador').empty();
      $('#divpuxador :input').prop('disabled', true);
    }
  }
});
</script>

<script>
$(document).ready(function() {
  // Função para verificar se os campos estão preenchidos
  function verificarCamposPreenchidos() {
    var quantidade = $('#id_quantidade').val();
    var largura = $('#id_largura').val();
    var altura = $('#id_altura').val();
    var acabamento = $('#id_acabamento').val();
    var abertura = $('#id_abertura').val();
    var perfil = $('#id_perfil').val();

    // Verificar se todos os campos estão preenchidos
    if (quantidade && largura && altura && acabamento && abertura) {
      // Desbloquear o campo perfil
      $('#id_perfil').prop('disabled', false);

      // Verificar se o campo perfil também está preenchido
      if (perfil) {
        // Desbloquear os demais campos na divportas
        $('#divportas input:not(#id_perfil), #divportas select:not(#id_perfil)').prop('disabled', false);
      } else {
        // Bloquear os demais campos na divportas
        $('#divportas input:not(#id_perfil), #divportas select:not(#id_perfil)').prop('disabled', true);
      }
    } else {
      // Bloquear os campos na divportas
      $('#divportas input, #divportas select').prop('disabled', true);
    }
  }

  // Verificar campos ao carregar a página
  verificarCamposPreenchidos();

  // Verificar campos sempre que houver uma alteração nos campos
  $('#id_quantidade, #id_largura, #id_altura, #id_acabamento, #id_abertura, #id_perfil').on('input', function() {
    verificarCamposPreenchidos();
  });
});
</script>

<script>
    function limparCampos() {
        // Selecionar os campos dentro da divportas
        var camposDivPortas = document.getElementById('divportas').getElementsByTagName('input');
        var selectsDivPortas = document.getElementById('divportas').getElementsByTagName('select');

        // Limpar os campos
        for (var i = 0; i < camposDivPortas.length; i++) {
            camposDivPortas[i].value = '';
        }
        for (var i = 0; i < selectsDivPortas.length; i++) {
            selectsDivPortas[i].value = '';
        }
    }
</script>




<script>
  document.addEventListener('DOMContentLoaded', function() {
    // Obtém referências para os elementos
    var btnPortaGiro = document.getElementById('btnPortaGiro');
    var btnPortaCorrer = document.getElementById('btnPortaCorrer');
    var btnDivisoria = document.getElementById('btnDivisoria');
    var btnVidro = document.getElementById('btnVidro');
    var campoLinha = document.getElementById('divlinha');
    var campoAcabamento = document.getElementById('divacabamento');
    var campoAbertura = document.getElementById('divabertura');

    // Adiciona o evento de mudança aos botões de rádio
    btnPortaGiro.addEventListener('change', function() {
      campoAcabamento.classList.remove('hidden');
      campoAbertura.classList.remove('hidden');
      campoLinha.classList.add('hidden');
    });

    btnPortaCorrer.addEventListener('change', function() {
      campoLinha.classList.add('hidden');
      campoAbertura.classList.add('hidden');
      campoAcabamento.classList.remove('hidden');
    });

    btnDivisoria.addEventListener('change', function() {
      campoAcabamento.classList.remove('hidden');
      campoLinha.classList.remove('hidden');
      campoAbertura.classList.add('hidden');
    });

    btnVidro.addEventListener('change', function() {
      campoLinha.classList.add('hidden');
      campoAbertura.classList.add('hidden');
      campoAcabamento.classList.add('hidden');
    });

    // Função para limpar o campo Linha
    function limparCampoLinha() {
      document.getElementById('id_linha').value = '';
    }
  });
</script>