//Escolha de div conforme o modelo de porta
const radioButtons = document.querySelectorAll('input[type="radio"][name="btnradio"]');
const div1 = document.getElementById("divportas");
const div2 = document.getElementById("divambiente");
const div3 = document.getElementById("divvidros");
const div4 = document.getElementById("divacabamento");
const div5 = document.getElementById("divabertura");
const div6 = document.getElementById("divlinha");


radioButtons.forEach(radio => {
  radio.addEventListener('change', function() {
    if (this.value === 'PortaGiro') {
      div1.style.display = "block";
      div2.style.display = "none";
      div3.style.display = "none";
      div4.style.display = "block";
      div5.style.display = "block";
      div6.style.display = "none";
    } else if (this.value === 'PortaCorrer') {
      div1.style.display = "block";
      div2.style.display = "none";
      div3.style.display = "none";
      div4.style.display = "block";
      div5.style.display = "block";
      div6.style.display = "none";
    } else if (this.value === 'DivisoriaAmbiente') {
      div1.style.display = "none";
      div2.style.display = "block";
      div3.style.display = "none";
      div4.style.display = "block";
      div5.style.display = "none";
      div6.style.display = "block";
    } else if (this.value === 'Vidros') {
      div1.style.display = "none";
      div2.style.display = "none";
      div3.style.display = "block";
      div4.style.display = "none";
      div5.style.display = "none";
      div6.style.display = "none";
    }
  });
});

