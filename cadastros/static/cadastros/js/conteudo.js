<script>
  $(document).ready(function() {
    $('#id_acabamento').change(function() {
      var acabamento = $(this).val(); // Obtenha o valor selecionado do acabamento

      $.ajax({
        url: '{% url 'filtrar_acabamento' %}',
        type: 'GET',
        data: {
          acabamento: acabamento
        },
        success: function(response) {
          $('#resultados_div').html(response); // Atualize a parte da página com os resultados filtrados
        },
        error: function(xhr) {
          console.log(xhr.statusText);
        }
      });
    });
  });
</script>