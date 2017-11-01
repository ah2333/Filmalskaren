// sköter den interaktiva sökfunktionen
function searchToggle(obj, evt){
    var container = $(obj).closest('.search-wrapper');

    if(!container.hasClass('active')){
          container.addClass('active');
          evt.preventDefault();
    }
    else if(container.hasClass('active') && $(obj).closest('.input-holder').length == 0){
          container.removeClass('active');
          // visar sökrutan och inputs kan skrivas
          container.find('.search-input').val('');
          // stänger ner sökrutan och blir en knapp
          container.find('.result-container').fadeOut(100, function(){$(this).empty();});
    }
}
