console.log("JavaScript carregado com sucesso na Vitrine Virtual!");

document.addEventListener('DOMContentLoaded', function () { //espera carregar o conteudo da pagina


  const swiper = new Swiper('.swiper', {                    // Inicia o Swiper

  effect: 'cube',
    cubeEffect: {
      shadow: true, 
      slideShadows: true, 
      shadowOffset: 20,
      shadowScale: 0.94,
    },
    
    direction: 'horizontal',                                // Direção do slider
    loop: true,                                             //Reiniciar carrossel ao chegar no final
    
      autoplay: {
      delay: 5000,                                          // Tempo
      disableOnInteraction: false,                          // Não para o autoplay quando o usuário interage
    },                                    
    pagination: {                                           // Bolinhas de paginação
      el: '.swiper-pagination',
      clickable: true,                                      // Permite clicar nas bolinhas para navegar
    },

    // Setas de navegação
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  });

});