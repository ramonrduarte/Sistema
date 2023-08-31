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

<script>
$(document).ready(function() {
  function atualizarPosicoesPerfilPuxador() {
    var qtdPerfilPuxador = $("#qtd-perfilpuxador").val();
    var perfilPuxador = $("#id_perfilpuxador").val();
    var abertura = $("#id_abertura").val();
    var posicaoPerfilPuxador = $("#posicao-perfilpuxador");

    posicaoPerfilPuxador.empty();

    if (qtdPerfilPuxador === "2") {
      if ($("#btnPortaCorrer").is(":checked")) {
        posicaoPerfilPuxador.append($('<option>', {value: 'Esq/Dir', text: 'Esq/Dir'}));
      }
    } else if (qtdPerfilPuxador === "1") {
        if ($("#btnPortaCorrer").is(":checked")) {
          posicaoPerfilPuxador.append($('<option>', {value: 'Direita', text: 'Direita'}));
          posicaoPerfilPuxador.append($('<option>', {value: 'Esquerda', text: 'Esquerda'}));
        } else if ($("#btnPortaGiro").is(":checked")) {
            if (abertura === "D") {
              posicaoPerfilPuxador.append($('<option>', {value: 'Esquerda', text: 'Esquerda'}));
              posicaoPerfilPuxador.append($('<option>', {value: 'Topo', text: 'Topo'}));
              posicaoPerfilPuxador.append($('<option>', {value: 'Base', text: 'Base'}));
            } else if (abertura === "E") {
              posicaoPerfilPuxador.append($('<option>', {value: 'Direita', text: 'Direita'}));
              posicaoPerfilPuxador.append($('<option>', {value: 'Topo', text: 'Topo'}));
              posicaoPerfilPuxador.append($('<option>', {value: 'Base', text: 'Base'}));
            } else if (abertura === "C") {
              posicaoPerfilPuxador.append($('<option>', {value: 'Base', text: 'Base'}));
            } else if (abertura === "B") {
              posicaoPerfilPuxador.append($('<option>', {value: 'Topo', text: 'Topo'}));
            }
        }
    }
  }

  function atualizarQtdPerfilPuxador() {
    var perfilPuxador = $("#id_perfilpuxador").val();
    var qtdPerfilPuxador = $("#qtd-perfilpuxador");

    qtdPerfilPuxador.empty();

    if ($("#btnPortaGiro").is(":checked")) {
      if (perfilPuxador && perfilPuxador !== "") {
        qtdPerfilPuxador.append($('<option>', {value: '1', text: '1'}));
      }
    } else if ($("#btnPortaCorrer").is(":checked")) {
      if (perfilPuxador && perfilPuxador !== "") {
        qtdPerfilPuxador.append($('<option>', {value: '1', text: '1'}));
        qtdPerfilPuxador.append($('<option>', {value: '2', text: '2'}));
      }
    }
  }

  $("#id_perfilpuxador").change(function() {
    atualizarQtdPerfilPuxador();
    atualizarPosicoesPerfilPuxador();
  });

  $("#qtd-perfilpuxador").change(function() {
    atualizarPosicoesPerfilPuxador();
  });

  $("#id_abertura").change(function() {
    atualizarPosicoesPerfilPuxador();
  });

  $("input[name='btnradio']").change(function() {
    atualizarQtdPerfilPuxador();
    atualizarPosicoesPerfilPuxador();
  });
});
</script>

<script>
$(document).ready(function() {
  function atualizarPosicoesPuxador() {
    var qtdPuxador = $("#qtd-puxador").val();
    var Puxador = $("#id_puxador").val();
    var abertura = $("#id_abertura").val();
    var posicaoPuxador = $("#posicao-puxador");

    posicaoPuxador.empty();

    if (qtdPuxador === "2") {
      if ($("#btnPortaCorrer").is(":checked")) {
        posicaoPuxador.append($('<option>', {value: 'Esq/Dir', text: 'Esq/Dir'}));
      }
    } else if (qtdPuxador === "1") {
        if ($("#btnPortaCorrer").is(":checked")) {
          posicaoPuxador.append($('<option>', {value: 'Direita', text: 'Direita'}));
          posicaoPuxador.append($('<option>', {value: 'Esquerda', text: 'Esquerda'}));
        } else if ($("#btnPortaGiro").is(":checked")) {
            if (abertura === "D") {
              posicaoPuxador.append($('<option>', {value: 'Esquerda', text: 'Esquerda'}));
              posicaoPuxador.append($('<option>', {value: 'Topo', text: 'Topo'}));
              posicaoPuxador.append($('<option>', {value: 'Base', text: 'Base'}));
            } else if (abertura === "E") {
              posicaoPuxador.append($('<option>', {value: 'Direita', text: 'Direita'}));
              posicaoPuxador.append($('<option>', {value: 'Topo', text: 'Topo'}));
              posicaoPuxador.append($('<option>', {value: 'Base', text: 'Base'}));
            } else if (abertura === "C") {
              posicaoPuxador.append($('<option>', {value: 'Base', text: 'Base'}));
            } else if (abertura === "B") {
              posicaoPuxador.append($('<option>', {value: 'Topo', text: 'Topo'}));
            }
        }
    }
  }

  function atualizarQtdPuxador() {
    var Puxador = $("#id_puxador").val();
    var qtdPuxador = $("#qtd-puxador");

    qtdPuxador.empty();

    if ($("#btnPortaGiro").is(":checked")) {
      if (Puxador && Puxador !== "") {
        qtdPuxador.append($('<option>', {value: '1', text: '1'}));
      }
    } else if ($("#btnPortaCorrer").is(":checked")) {
      if (Puxador && Puxador !== "") {
        qtdPuxador.append($('<option>', {value: '1', text: '1'}));
        qtdPuxador.append($('<option>', {value: '2', text: '2'}));
      }
    }
  }

  $("#id_puxador").change(function() {
    atualizarQtdPuxador();
    atualizarPosicoesPuxador();
  });

  $("#qtd-puxador").change(function() {
    atualizarPosicoesPuxador();
  });

  $("#id_abertura").change(function() {
    atualizarPosicoesPuxador();
  });

  $("input[name='btnradio']").change(function() {
    atualizarQtdPuxador();
    atualizarPosicoesPuxador();
  });
});
</script>

<script>
$(document).ready(function() {
  $('#id_acabamento, #id_quantidade, #id_largura, #id_altura, #id_abertura').change(filtrarPerfil);

  function filtrarPerfil() {
    var acabamento = $('#id_acabamento').val();
    var quantidade = $('#id_quantidade').val();
    var largura = $('#id_largura').val();
    var altura = $('#id_altura').val();
    var abertura = $('#id_abertura').val();
    var perfilField = $('#id_perfil');
    var perfilDiv = $('#divperfil');
    var campoPortas = $('#divportas');
    var portaGiroRadioButton = $('#btnPortaGiro');
    var portaCorrerRadioButton = $('#btnPortaCorrer');

    // Verificar se o radiobutton selecionado é PortaGiro
    if (portaGiroRadioButton.is(':checked')) {
      if (quantidade && largura && altura && acabamento && abertura) {
        perfilField.prop('disabled', false);
        perfilDiv.find(':input').prop('disabled', false);

        $.ajax({
          url: '/filtrar_acabamento/',
          type: 'GET',
          data: {
            acabamento: acabamento
          },
          success: function(response) {
            perfilField.empty();

            var option = $('<option>').attr('value', '').text('-------');
            perfilField.append(option);

            $.each(response, function(index, item) {
              option = $('<option>').attr('value', item.id).text(item.descricao);
              perfilField.append(option);
            });

            perfilField.show();
          },
          error: function(xhr) {
            console.log(xhr.statusText);
          }
        });
      } else {
        campoPortas.prop('disabled', true);
        campoPortas.find(':input').prop('disabled', true);
        perfilField.empty();
      }
    } else if (portaCorrerRadioButton.is(':checked')) {
      if (quantidade && largura && altura && acabamento) {
        perfilField.prop('disabled', false);
        perfilDiv.find(':input').prop('disabled', false);

        $.ajax({
          url: '/filtrar_acabamento/',
          type: 'GET',
          data: {
            acabamento: acabamento
          },
          success: function(response) {
            perfilField.empty();

            var option = $('<option>').attr('value', '').text('-------');
            perfilField.append(option);

            $.each(response, function(index, item) {
              option = $('<option>').attr('value', item.id).text(item.descricao);
              perfilField.append(option);
            });

            perfilField.show();
          },
          error: function(xhr) {
            console.log(xhr.statusText);
          }
        });
      }
    } else {
      // Manter o campo perfil bloqueado para outros radiobuttons selecionados
      perfilField.prop('disabled', true);
      perfilDiv.find(':input').prop('disabled', true);
      perfilField.empty();
    }
  }

  // Chamar a função filtrarPerfil inicialmente
  filtrarPerfil();
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
        url: '/buscar_PerfilPuxador/',
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

          var numItens = response.length;

          if (numItens <= 0) {
            selectPerfilPuxador.prop('disabled', true);
            $('#divperfilpuxador :input').prop('disabled', true);
          } else {
            selectPerfilPuxador.prop('disabled', false);
            $('#divperfilpuxador :input').prop('disabled', false);
          }

          selectPerfilPuxador.show();
        },
        error: function(xhr) {
          console.log(xhr.statusText);
        }
      });
    } else {
      $('#id_perfilpuxador').empty();
      $('#divperfilpuxador :input').prop('disabled', true);
    }
  }
});
</script>

<script>
$(document).ready(function() {
  $('#id_perfil').change(function() {
    limparCamposPortas();
    buscarDivisor();
    limparCampoVidro();
  });

  function buscarDivisor() {
    var perfil = $('#id_perfil').val();

    if (perfil) {
      $.ajax({
        url: '/buscar_Divisor/',
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

          var numItens = response.length;

          if (numItens <= 0) {
            selectDivisor.prop('disabled', true);
            $('#divdivisor :input').prop('disabled', true);
          } else {
            selectDivisor.prop('disabled', false);
            $('#divdivisor :input').prop('disabled', false);
          }

          selectDivisor.show();
        },
        error: function(xhr) {
          console.log(xhr.statusText);
        }
      });
    } else {
      $('#id_divisor').empty();
      $('#divdivisor :input').prop('disabled', true);
    }
  }

  function limparCamposPortas() {
    $('#divportas input:not(#id_perfil), #divportas select:not(#id_perfil)').each(function() {
      $(this).val('').prop('disabled', true);
    });
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
        url: '/buscar_Puxador/',
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

          var numItens = response.length;

          if (numItens <= 0) {
            selectPuxador.prop('disabled', true);
            $('#divpuxador :input').prop('disabled', true);
          } else {
            selectPuxador.prop('disabled', false);
            $('#divpuxador :input').prop('disabled', false);
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
  $('#id_perfil').change(function() {
    buscarVidro();
  });

  function buscarVidro() {
  var perfil = $('#id_perfil').val();

  if (perfil) {
    var vidro = $('#id_vidro').val();

    $.ajax({
      url: '/buscar_Vidro/',
      type: 'GET',
      data: {
        vidro: vidro
      },
      success: function(response) {
        var selectVidro = $('#id_vidro');
        selectVidro.empty();

        var option = $('<option>').attr('value', '').text('-------');
        selectVidro.append(option);

        $.each(response, function(index, item) {
          option = $('<option>').attr('value', item.id).text(item.descricao);
          selectVidro.append(option);
        });

        var numItens = response.length;

        if (numItens <= 0) {
          selectVidro.prop('disabled', true);
          $('#divvidro :input').prop('disabled', true);
        } else {
          selectVidro.prop('disabled', false);
          $('#divvidro :input').prop('disabled', false);
        }

        selectVidro.show();
      },
      error: function(xhr) {
        console.log(xhr.statusText);
      }
    });
  } else {
    $('#id_vidro').empty();
    $('#divvidro :input').prop('disabled', true);
  }
}
});
</script>

<script>
$(document).ready(function() {
  $('#id_acabamento, #id_abertura').change(function() {
    // Limpar e bloquear os campos da divportas, exceto o campo perfil
    $('#divportas input:not(#id_perfil), #divportas select:not(#id_perfil)').val('').prop('disabled', true);

    // Verificar se os campos obrigatórios estão preenchidos
    var quantidade = $('#id_quantidade').val();
    var largura = $('#id_largura').val();
    var altura = $('#id_altura').val();
    var acabamento = $('#id_acabamento').val();
    var abertura = $('#id_abertura').val();

    if ($('#btnPortaGiro').is(':checked')) {
        if (quantidade && largura && altura && acabamento && abertura) {
          // Desbloquear o campo perfil
          $('#id_perfil').prop('disabled', false);
        }
    }
    if ($('#btnPortaCorrer').is(':checked')) {
        if (quantidade && largura && altura && acabamento) {
          // Desbloquear o campo perfil
          $('#id_perfil').prop('disabled', false);
        }
    }
  });
});
</script>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    var btnPortaGiro = document.getElementById('btnPortaGiro');
    var btnPortaCorrer = document.getElementById('btnPortaCorrer');
    var btnDivisoria = document.getElementById('btnDivisoria');
    var btnVidro = document.getElementById('btnVidro');
    var campoLinha = document.getElementById('divlinha');
    var campoAcabamento = document.getElementById('divacabamento');
    var campoAbertura = document.getElementById('divabertura');
    var campoPorta = document.getElementById('divportas');
    var campoDivisoria = document.getElementById('divambiente');
    var campoVidro = document.getElementById('divvidros');

    btnPortaGiro.addEventListener('change', function() {
      limparCampos();
      campoAcabamento.classList.remove('d-none');
      campoAbertura.classList.remove('d-none');
      campoLinha.classList.add('d-none');
      campoPorta.classList.remove('hidden');
      campoDivisoria.classList.add('hidden');
      campoVidro.classList.add('hidden');
    });

    btnPortaCorrer.addEventListener('change', function() {
      limparCampos();
      campoLinha.classList.add('d-none');
      campoAbertura.classList.add('d-none');
      campoAcabamento.classList.remove('d-none');
      campoPorta.classList.remove('hidden');
      campoDivisoria.classList.add('hidden');
      campoVidro.classList.add('hidden');
    });

    btnDivisoria.addEventListener('change', function() {
      limparCampos();
      campoAcabamento.classList.remove('d-none');
      campoLinha.classList.remove('d-none');
      campoAbertura.classList.add('d-none');
      campoPorta.classList.add('hidden');
      campoDivisoria.classList.remove('hidden');
      campoVidro.classList.add('hidden');
    });

    btnVidro.addEventListener('change', function() {
      limparCampos();
      campoLinha.classList.add('d-none');
      campoAbertura.classList.add('d-none');
      campoAcabamento.classList.add('d-none');
      campoPorta.classList.add('hidden');
      campoDivisoria.classList.add('hidden');
      campoVidro.classList.remove('hidden');
    });

    function limparCampos() {
      var camposPorta = document.getElementById('divportas').getElementsByTagName('input');
      var selectsPorta = document.getElementById('divportas').getElementsByTagName('select');

      for (var i = 0; i < camposPorta.length; i++) {
        camposPorta[i].value = '';
        camposPorta[i].disabled = true;
      }
      for (var i = 0; i < selectsPorta.length; i++) {
        selectsPorta[i].value = '';
        selectsPorta[i].disabled = true;
      }

      var camposDivisoria = document.getElementById('divambiente').getElementsByTagName('input');
      var selectsDivisoria = document.getElementById('divambiente').getElementsByTagName('select');

      for (var i = 0; i < camposDivisoria.length; i++) {
        camposDivisoria[i].value = '';
        camposDivisoria[i].disabled = true;
      }
      for (var i = 0; i < selectsDivisoria.length; i++) {
        selectsDivisoria[i].value = '';
        selectsDivisoria[i].disabled = true;
      }

      var camposVidro = document.getElementById('divvidros').getElementsByTagName('input');
      var selectsVidro = document.getElementById('divvidros').getElementsByTagName('select');

      for (var i = 0; i < camposVidro.length; i++) {
        camposVidro[i].value = '';
        camposVidro[i].disabled = true;
      }
      for (var i = 0; i < selectsVidro.length; i++) {
        selectsVidro[i].value = '';
      }

      var campoAcabamento = document.getElementById('id_acabamento');
      var campoAbertura = document.getElementById('id_abertura');
      var campoLinha = document.getElementById('id_linha');

      campoAcabamento.value = '';
      campoAcabamento.disabled = false;

      campoAbertura.value = '';
      campoAbertura.disabled = false;

      campoLinha.value = '';
      campoLinha.disabled = false;
    }
  });
</script>

<script>
  $(document).ready(function() {
    $("#id_perfilpuxador").change(function() {
      var perfilPuxador = $(this).val();
      var puxadorField = $("#id_puxador");
      var qtdpuxadorField = $("#qtd-puxador");
      var posicaopuxadorField = $("#posicao-puxador");
      var tamanhopuxadorField = $("#tam-puxador");

      if (perfilPuxador && perfilPuxador !== "") {
      puxadorField.prop('disabled', true);
      qtdpuxadorField.prop('disabled', true);
      posicaopuxadorField.prop('disabled', true);
      tamanhopuxadorField.prop('disabled', true);
      } else {
        if (puxadorField.children().length > 1) {
            puxadorField.prop('disabled', false);
            qtdpuxadorField.prop('disabled', false);
            posicaopuxadorField.prop('disabled', false);
            tamanhopuxadorField.prop('disabled', false);
        }
      }

      // Clear the related fields
      $("#qtd-perfilpuxador").val('');
      $("#posicao-perfilpuxador").val('');
    });

    $("#id_puxador").change(function() {
      var puxador = $(this).val();
      var perfilPuxadorField = $("#id_perfilpuxador");
      var qtdperfilPuxadorField = $("#qtd-perfilpuxador");
      var posicaoperfilPuxadorField = $("#posicao-perfilpuxador");

      if (puxador && puxador !== "") {
      perfilPuxadorField.prop('disabled', true);
      qtdperfilPuxadorField.prop('disabled', true);
      posicaoperfilPuxadorField.prop('disabled', true);
      } else {
        if (perfilPuxadorField.children().length > 1) {
            perfilPuxadorField.prop('disabled', false);
            qtdperfilPuxadorField.prop('disabled', false);
            posicaoperfilPuxadorField.prop('disabled', false);
        }
      }

      $("#qtd-puxador").val('');
      $("#posicao-puxador").val('');
      $("#tam-puxador").val('');
    });

    $("#id_perfil").change(function() {
      var perfil = $(this).val();
      var campoVidro = $("#id_vidro");

      if (perfil && perfil !== "") {
        campoVidro.prop('disabled', false);
      } else {
        campoVidro.prop('disabled', true);
      }
    });
  });
</script>

<script>
$(document).ready(function() {

  $("#id_divisor").change(function() {
    var divisor = $(this).val();
    var qtdDivisor = $("#qtd-divisor");

    qtdDivisor.empty();

    if (divisor && divisor !== "") {
      qtdDivisor.empty();
      qtdDivisor.append($('<option>', {value: '1', text: '1'}));
      qtdDivisor.append($('<option>', {value: '2', text: '2'}));
      qtdDivisor.prop('disabled', false);
    }
  });
});
</script>

<script>
$(document).ready(function() {

  $("#Selectambientedivisor").change(function() {
    var divisor = $(this).val();
    var qtdDivisor = $("#qtd-divisorambiente");

    qtdDivisor.empty();

    if (divisor && divisor !== "") {
      qtdDivisor.empty();
      qtdDivisor.append($('<option>', {value: '1', text: '1'}));
      qtdDivisor.append($('<option>', {value: '2', text: '2'}));
      qtdDivisor.prop('disabled', false);
    }
  });
});
</script>

<script>
$(document).ready(function() {
  // Funções reutilizáveis
  function carregarOpcoes(selectElement, data) {
    selectElement.empty();
    var option = $('<option>').attr('value', '').text('-------');
    selectElement.append(option);

    if (data.length > 0) {
      $.each(data, function(index, item) {
        option = $('<option>').attr('value', item.id).text(item.descricao);
        selectElement.append(option);
      });

      selectElement.prop('disabled', false);
      selectElement.show();
    } else {
      selectElement.prop('disabled', true);
    }
  }

  function realizarRequisicao(url, params, successCallback) {
    $.ajax({
      url: url,
      type: 'GET',
      data: params,
      success: successCallback,
      error: function(xhr) {
        console.log(xhr.statusText);
      }
    });
  }

  // Filtrar Divisoria
  $('#id_acabamento, #id_quantidade, #id_largura, #id_altura, #id_linha').change(filtrarDivisoria);

  function filtrarDivisoria() {
    var acabamento = $('#id_acabamento').val();
    var quantidade = $('#id_quantidade').val();
    var largura = $('#id_largura').val();
    var altura = $('#id_altura').val();
    var linha = $('#id_linha').val();
    var divsuperiorField = $('#Selectambientesuperior');
    var divinferiorField = $('#Selectambienteinferior');
    var divlateralField = $('#Selectambientelateral');
    var divdivisorField = $('#Selectambientedivisor');
    var campoDivisoria = $('#divambiente');
    var divisoriaRadioButton = $('#btnDivisoria');
    var idDivisoriaAmbiente = $('#id_divisoriaambiente');

    if (divisoriaRadioButton.is(':checked')) {
      if (quantidade && largura && altura && acabamento && linha) {
        divsuperiorField.prop('disabled', false);
        idDivisoriaAmbiente.find(':input').prop('disabled', false);

        realizarRequisicao('/filtrar_divisoria/', { acabamento: acabamento, linha: linha }, function(response) {
          carregarOpcoes(divsuperiorField, response);
          carregarDivinferior(acabamento, linha);
          carregarDivlateral(acabamento, linha);
          carregarDivdivisor(acabamento, linha);
        });
      } else {
        idDivisoriaAmbiente.prop('disabled', true);
        idDivisoriaAmbiente.find(':input').prop('disabled', true);
      }
    } else {
      idDivisoriaAmbiente.prop('disabled', true);
      idDivisoriaAmbiente.find(':input').prop('disabled', true);
    }
  }

  // Carregar Divinferior
  function carregarDivinferior(acabamento, linha) {
    var divinferiorField = $('#Selectambienteinferior');

    realizarRequisicao('/carregar_divinferior/', { acabamento: acabamento, linha: linha }, function(response) {
      carregarOpcoes(divinferiorField, response);
    });
  }

  // Carregar Divlateral
  function carregarDivlateral(acabamento, linha) {
    var divlateralField = $('#Selectambientelateral');

    realizarRequisicao('/carregar_divlateral/', { acabamento: acabamento, linha: linha }, function(response) {
      carregarOpcoes(divlateralField, response);
    });
  }

  // Carregar Divdivisor
  function carregarDivdivisor(acabamento, linha) {
    var divdivisorField = $('#Selectambientedivisor');

    realizarRequisicao('/carregar_divdivisor/', { acabamento: acabamento, linha: linha }, function(response) {
      carregarOpcoes(divdivisorField, response);
    });
  }

  // Obter acabamentos DivisoriaAmbiente
  $('#btnDivisoria').change(obterAcabamentosDivisoriaAmbiente);

  function obterAcabamentosDivisoriaAmbiente() {
    realizarRequisicao('/obter_acabamentos_divisoria_ambiente/', {}, function(response) {
      var selectAcabamento = $('#id_acabamento');
      selectAcabamento.empty();

      if (response.acabamentos.length > 0) {
        $.each(response.acabamentos, function(index, item) {
          var option = $('<option>').attr('value', item.id).text(item.acabamento);
          selectAcabamento.append(option);
        });

        selectAcabamento.prop('disabled', false);
        selectAcabamento.show();
      } else {
        selectAcabamento.prop('disabled', true);
        selectAcabamento.hide();
      }
    });
  }

  // Buscar Vidro
  $('#Selectambientesuperior').change(buscarVidro);

  function buscarVidro() {
    var divsuperior = $('#Selectambientesuperior').val();

    if (divsuperior) {
      var vidro = $('#Selectambientevidro').val();

      realizarRequisicao('/buscar_Vidro/', { vidro: vidro }, function(response) {
        var selectVidro = $('#Selectambientevidro');
        carregarOpcoes(selectVidro, response);

        if (response.length > 0) {
          selectVidro.prop('disabled', false);
          selectVidro.show();
        } else {
          selectVidro.prop('disabled', true);
          selectVidro.hide();
        }
      });
    } else {
      $('#Selectambientevidro').empty();
      $('#divambientevidro :input').prop('disabled', true);
    }
  }

  filtrarDivisoria();
});

</script>

<!--<script>-->
<!--  document.addEventListener("DOMContentLoaded", function () {-->
<!--    const svgObject = document.getElementById("svgObject");-->

<!--    // Carregar o SVG e adicionar evento de carregamento-->
<!--    svgObject.addEventListener("load", function () {-->
<!--      const svgDocument = svgObject.contentDocument; // Acessar o conteúdo do SVG-->

<!--      // Função para adicionar ou remover classes de acordo com o valor do elemento "id_perfil"-->
<!--      function ajustarClassesDoPerfil() {-->
<!--        const idPerfil = document.getElementById("id_perfil").value;-->

<!--        // Selecionar os elementos pelos seus ids-->
<!--        const perfSuperior = svgDocument.getElementById("Perf-Superior");-->
<!--        const perfInferior = svgDocument.getElementById("Perf-Inferior");-->
<!--        const perfDireita = svgDocument.getElementById("Perf-Direita");-->
<!--        const perfEsquerda = svgDocument.getElementById("Perf-Esquerda");-->
<!--        const MedidaDesenho = svgDocument.getElementById("Medida_Desenho");-->

<!--        // Verificar se o valor do elemento com id="id_perfil" está vazio-->
<!--        if (idPerfil === "") {-->
<!--          // Caso esteja vazio, ocultar com a classe st3 e remover a classe st9-->
<!--          perfSuperior.classList.add("st3");-->
<!--          perfSuperior.classList.remove("st9");-->

<!--          perfInferior.classList.add("st3");-->
<!--          perfInferior.classList.remove("st9");-->

<!--          perfDireita.classList.add("st3");-->
<!--          perfDireita.classList.remove("st9");-->

<!--          perfEsquerda.classList.add("st3");-->
<!--          perfEsquerda.classList.remove("st9");-->

<!--          MedidaDesenho.classList.add("st3");-->
<!--          MedidaDesenho.classList.remove("st9");-->

<!--          // Atualizar medidas no SVG quando o perfil estiver vazio-->
<!--          const alturaInput = document.getElementById("id_altura");-->
<!--          const larguraInput = document.getElementById("id_largura");-->
<!--          const medidaAlturaText = svgDocument.getElementById("Medida-altura");-->
<!--          const medidaLarguraText = svgDocument.getElementById("Medida-largura");-->

<!--          atualizarMedida(alturaInput, medidaAlturaText);-->
<!--          atualizarMedida(larguraInput, medidaLarguraText);-->
<!--        } else {-->
<!--          // Caso tenha um valor selecionado, remover a classe st3 e adicionar a classe st9-->
<!--          perfSuperior.classList.remove("st3");-->
<!--          perfSuperior.classList.add("st9");-->

<!--          perfInferior.classList.remove("st3");-->
<!--          perfInferior.classList.add("st9");-->

<!--          perfDireita.classList.remove("st3");-->
<!--          perfDireita.classList.add("st9");-->

<!--          perfEsquerda.classList.remove("st3");-->
<!--          perfEsquerda.classList.add("st9");-->

<!--          MedidaDesenho.classList.remove("st3");-->
<!--          MedidaDesenho.classList.add("st9");-->
<!--        }-->
<!--      }-->

<!--      // Adicionar um evento para detectar mudanças no valor do elemento com id="id_perfil"-->
<!--      document.getElementById("id_perfil").addEventListener("change", ajustarClassesDoPerfil);-->

<!--      // Chamar a função inicialmente para configurar as classes de acordo com o valor inicial-->
<!--      ajustarClassesDoPerfil();-->

<!--      // Atualizar as medidas quando o perfil for carregado-->
<!--      const alturaInput = document.getElementById("id_altura");-->
<!--      const larguraInput = document.getElementById("id_largura");-->
<!--      const medidaAlturaText = svgDocument.getElementById("Medida-altura");-->
<!--      const medidaLarguraText = svgDocument.getElementById("Medida-largura");-->

<!--      alturaInput.addEventListener("input", function () {-->
<!--        atualizarMedida(alturaInput, medidaAlturaText);-->
<!--      });-->

<!--      larguraInput.addEventListener("input", function () {-->
<!--        atualizarMedida(larguraInput, medidaLarguraText);-->
<!--      });-->
<!--    });-->
<!--  });-->

<!--  // Função para atualizar a medida no campo de texto do SVG-->
<!--  function atualizarMedida(campoInput, campoMedida) {-->
<!--    const valor = campoInput.value;-->
<!--    if (campoMedida) {-->
<!--      campoMedida.textContent = valor + "mm";-->
<!--    }-->
<!--  }-->
<!--</script>-->
